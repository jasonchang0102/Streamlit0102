/*
Database Schema Discovery — SQL Server
Used before every schema migration to catalog all tables, PKs, FKs,
and column descriptions across all databases.
Maps the full estate so downstream dashboard impact is known BEFORE changes.
*/
IF OBJECT_ID('tempdb..##AllTables') IS NULL
BEGIN
    CREATE TABLE ##AllTables (
        DatabaseName sysname,
        SchemaName sysname NULL,
        TableName sysname,
        PrimaryKeyColumn sysname NULL,
        ForeignKeyColumn sysname NULL,
        ColumnName sysname NULL,
        ColumnDescription NVARCHAR(MAX) NULL
    );
END

EXEC sp_MSforeachdb '
    USE [?];
    INSERT INTO ##AllTables
    SELECT DB_NAME(), SCHEMA_NAME(), t.name,
        (SELECT TOP 1 c.name FROM sys.indexes i
         JOIN sys.index_columns ic ON i.object_id = ic.object_id
         JOIN sys.columns c ON c.object_id = t.object_id
            AND c.column_id = ic.column_id
         WHERE i.is_primary_key = 1 AND i.object_id = t.object_id),
        (SELECT TOP 1 c.name FROM sys.foreign_key_columns fkc
         JOIN sys.columns c ON c.object_id = t.object_id
            AND c.column_id = fkc.parent_column_id),
        C.name,
        CONVERT(NVARCHAR(MAX), ep.value)
    FROM sys.tables t
    JOIN sys.columns C ON C.object_id = T.object_id
    LEFT JOIN sys.extended_properties ep
        ON ep.major_id = C.object_id AND ep.minor_id = C.column_id;
'
SELECT * FROM ##AllTables;
