-- Content: SQL query to calculate the change in streams and chart position for Lady Gaga
SELECT
   artist,
   week,
   streams_millions,
   streams_millions - LAG(streams_millions, 1, streams_millions) OVER ( 
      PARTITION BY artist
      ORDER BY week DESC
   ) AS 'streams_millions_change',
   chart_position,
   LAG(chart_position, 1, chart_position) OVER ( 
      PARTITION BY artist
      ORDER BY week 
) - chart_position AS 'chart_position_change'
FROM
   streams
WHERE 
   artist = 'Lady Gaga';


-- Compare Funnels For A/B Tests
SELECT * FROM onboarding_modals LIMIT 10;

SELECT modal_text, COUNT(DISTINCT user_id)
FROM onboarding_modals
GROUP BY modal_text
ORDER BY modal_text;

SELECT modal_text,
  COUNT(DISTINCT CASE
    WHEN ab_group = 'control' THEN user_id
    END) AS 'control_clicks',
    COUNT(DISTINCT CASE
    WHEN ab_group = 'variant' THEN user_id
    END) AS 'variant_clicks'
FROM onboarding_modals
GROUP BY 1
ORDER BY 1;

-- Build a Funnel from Multiple Tables 2
WITH funnels AS (
  SELECT DISTINCT b.browse_date,
     b.user_id,
     c.user_id IS NOT NULL AS 'is_checkout',
     p.user_id IS NOT NULL AS 'is_purchase'
  FROM browse AS 'b'
  LEFT JOIN checkout AS 'c'
    ON c.user_id = b.user_id
  LEFT JOIN purchase AS 'p'
    ON p.user_id = c.user_id)
SELECT COUNT(*) AS 'num_browse',
   SUM(is_checkout) AS 'num_checkout',
   SUM(is_purchase) AS 'num_purchase',
   1.0 * SUM(is_checkout) / COUNT(user_id) AS 'browse_to_checkout',
   1.0 * SUM(is_purchase) / SUM(is_checkout) AS 'checkout_to_purchase'
FROM funnels;

-- Calculate Churn Rate
SELECT 1.0 * 
(
  SELECT COUNT(*)
  FROM subscriptions
  WHERE subscription_start < '2017-01-01'
  AND (
    subscription_end
    BETWEEN '2017-01-01'
    AND '2017-01-31'
  )
) / (
  SELECT COUNT(*) 
  FROM subscriptions 
  WHERE subscription_start < '2017-01-01'
  AND (
    (subscription_end >= '2017-01-01') -- 
    OR (subscription_end IS NULL)
  )
) 
AS result;

