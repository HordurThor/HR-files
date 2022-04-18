CREATE TRIGGER WASP_Schema.Check_Grant
ON Grants
After INSERT
AS
BEGIN 
    IF EXISTS(SELECT Date, MemID FROM Grants)
    BEGIN
        ROLLBACK TRANSACTION
        RAISERROR('Member has already been granted today')
    End
End; 