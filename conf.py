DB_NAME = 'mock_resq.db'

CREATE_TABLE_QUERY = """
CREATE TABLE presentation (
    user TEXT,
    currency TEXT,
    total_sales REAL,
    purchase_number INTEGER,
    favorite_segment TEXT,
    M0_cohort TEXT,
    M1_retention INTEGER,
    lifespan_days INTEGER);
"""

INSERT_QUERY = """
INSERT INTO presentation (user, currency, total_sales, purchase_number, favorite_segment, M0_cohort, M1_retention, lifespan_days)
VALUES (?, ?, ?, ?, ?, ?, ?, ?);
"""

REMOVE_TABLE_QUERY = """
DROP TABLE IF EXISTS presentation;
"""

TRANSFORM_QUERY = """
WITH aggregated_offer_types AS
(
    SELECT o.userId as user_id, 
           p.defaultOfferType as offer_type, 
           count(*) as cnt
    FROM orders o 
    LEFT JOIN providers p ON p.id = o.providerId
    WHERE refunded != 1
    GROUP BY 1, 2
),
ranked_offer_types AS
(
    SELECT *,
           row_number() OVER (PARTITION BY user_id ORDER BY cnt DESC) as rn
    FROM aggregated_offer_types
),
favorite_offer_types AS (
    SELECT user_id, offer_type, cnt
    FROM ranked_offer_types
    WHERE rn = 1
)
SELECT o.userId as user_id,
       o.currency as currency,
       SUM(o.sales) as total_sales,
       COUNT(*) as purchase_number,
       f.offer_type as favorite_segment,
       STRFTIME('%Y-%m', MIN(o.createdAt)) AS M0_cohort,
       CASE
           WHEN (JULIANDAY(MAX(o.createdAt)) - JULIANDAY(MIN(o.createdAt))) > 30 THEN 1
           ELSE 0
       END as M1_retention,
       ROUND(JULIANDAY(MAX(o.createdAt)) - JULIANDAY(MIN(o.createdAt)), 0) as lifespan_days
FROM orders o
LEFT JOIN favorite_offer_types f ON f.user_id = o.userId
WHERE o.refunded != 1
GROUP BY 1, 2;
"""
