

def PrintSQL(Att1, Att2):
    print ("""
SELECT 'Customers: %s --> %s' AS FD,
CASE WHEN COUNT(*)=0 THEN 'MAY HOLD'
ELSE 'does not hold' END AS VALIDITY
FROM (
    SELECT R.%s
    FROM Customers R
    GROUP BY R.%s
    HAVING COUNT(DISTINCT R.%s) > 1
) X;
""" % (Att1, Att2, Att1, Att1, Att2))

R = ['CID', 'CN', 'CS', 'CNr', 'CZ', 'CC', 'EID']
for i in range(len(R)):
    for j in range(len(R)):
        if (i != j):
            PrintSQL(R[i], R[j])