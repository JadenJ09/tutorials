### Information Schema: To know structure of tables with keys attribute: primary key, foreign keys
Primary Key:
A primary key ensures that every row of a table has a unique and non-null identifier.
You can define a primary key on single or multiple columns.
It is a database constraint available in all relational databases.

Unique:
A unique key ensures the uniqueness of values in a column or set of columns.
Unlike a primary key, a unique key can contain null values (with some restrictions).
A table can have multiple unique keys, but only one primary key.
Both primary and unique keys can be used as foreign keys.

SELECT
  constraint_name, table_name, column_name
FROM
  information_schema.key_column_usage
WHERE
  table_name = 'book';

SELECT
  constraint_name, table_name, column_name
FROM
  information_schema.key_column_usage
WHERE
  table_name = 'chapter';

SELECT
  constraint_name, table_name, column_name
FROM
  information_schema.key_column_usage
WHERE
  table_name = 'author';


### Database Relationship
- One-to-One Relationship
CREATE TABLE driver (
    license_id char(20) PRIMARY KEY,
    name varchar(20),
    address varchar(100),
    date_of_birth date
);      

CREATE TABLE license (
    id integer PRIMARY KEY,
    state_issued varchar(20),
    date_issued date,
    date_expired  date,
    license_id char(20) REFERENCES driver(license_id) UNIQUE
); 

- One-to-Many Relationship: A parent with many child tables linked as foreign keys

- Many-to-Many Relationship
CREATE TABLE books_authors (
  book_isbn varchar(50) REFERENCES book(isbn),
  author_email varchar(20) REFERENCES author(email)
  PRIMARY KEY (book_isbn, author_email)
);

SELECT book.title as book_title, author.name as author_name, book.description as book_description
FROM book
INNER JOIN books_authors
ON book.isbn = books_authors.book_isbn
INNER JOIN author
ON books_authors.author_email = author.email 

#### WITH AS()
It creates a temporal sub table


### PostgreSQL
#### NULL Constraints
- IS NOT NULL is for querying existing data.
- SET NOT NULL is for defining constraints on columns.
- DROP NOT NULL is for removing the constraint.

#### CHECK Constraints
CREATE TABLE Persons (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
    CHECK (Age >= 18)
);

If you already have a table and want to add a CHECK constraint, you can use the ALTER TABLE statement. For example:
ALTER TABLE Persons ADD CHECK (Age >= 18);

To give your CHECK constraint a name (useful for referencing it later), you can use the following syntax:
ALTER TABLE Persons ADD CONSTRAINT CHK_PersonAge CHECK (Age >= 18 AND City = 'Sandnes');

If you need to remove a CHECK constraint, use the following SQL:
ALTER TABLE Persons DROP CONSTRAINT CHK_PersonAge;
ALTER TABLE Persons DROP CHECK CHK_PersonAge;

#### UNIQUE / Primary & Foreign key Constraints
ALTER TABLE talks
ADD UNIQUE (speaker_id, session_timeslot) #on multiple columns

ALTER TABLE attendees
ADD PRIMARY KEY (id); 

ALTER TABLE registrations
ADD FOREIGN KEY (talk_id)
REFERENCES talks (id);

ALTER TABLE registrations
ADD FOREIGN KEY (talk_id)
REFERENCES talks (id) ON DELETE CASCADE #Cascading changes, when the parent's row deleted, automatically delete childeren's rows

ALTER TABLE talks
ADD FOREIGN KEY (speaker_id)
REFERENCES speakers (id) ON DELETE CASCADE;

DELETE FROM speakers 
WHERE id = 2;


### Window Functions
Window functions allow you to maintain the values of your original table while displaying grouped or summative information alongside in another column. Not like GROUP BY

- FIRST_VALUE() returns the first value in an ordered set of values.
- LAST_VALUE() returns the last value in an ordered set of values.

SELECT username,
   posts,
   LAST_VALUE (posts) OVER ( #LAST_VALUE can be functions
      PARTITION BY username  #similar with pandas's groupby
      ORDER BY posts
      RANGE BETWEEN UNBOUNDED PRECEDING AND 
      UNBOUNDED FOLLOWING
   ) AS 'most_posts'
FROM social_media;

SELECT 
   month,
   change_in_followers,
   SUM(change_in_followers) OVER (
      ORDER BY month
   ) AS 'running_total',
   AVG(change_in_followers) OVER (
      ORDER BY month
   ) AS 'running_avg',
   COUNT(change_in_followers) OVER (
      ORDER BY month
   ) AS 'running_count'
FROM
   social_media
WHERE
   username = 'instagram';

- Window functions can use LAG or LEAD in order to access information from a row at a specified offset which comes before (LAG) or after (LEAD) the current row.

SELECT
   artist,
   week,
   streams_millions,
   streams_millions - LAG(streams_millions, 1, streams_millions) OVER ( 
      PARTITION BY artist
      ORDER BY week 
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

SELECT
   artist,
   week,
   streams_millions,
   LEAD(streams_millions, 1) OVER (
      PARTITION BY artist
      ORDER BY week
   ) - streams_millions AS 'streams_millions_change',
   chart_position,
   chart_position - LEAD(chart_position, 1) OVER (
    PARTITION BY artist
    ORDER BY week
   ) AS 'chart_position_change'
FROM
   streams;

- ROW_NUMBER(): it inserts a sequential integer number to each row
SELECT 
   ROW_NUMBER() OVER (
      ORDER BY streams_millions DESC
   ) AS 'row_num', 
   artist, 
   week,
   streams_millions
FROM
   streams;

- RANK(): Not like ROW_NUMBER(), it allows same ranks, numbers
SELECT 
   RANK() OVER (
      PARTITION BY week
      ORDER BY streams_millions DESC
   ) AS 'rank', 
   artist, 
   week,
   streams_millions
FROM
   streams;

- NTILE(n): it makes n' tiles in order.
SELECT 
   NTILE(4) OVER (
      PARTITION BY week
      ORDER BY streams_millions DESC
   ) AS 'quartile', 
   artist, 
   week,
   streams_millions
FROM
   streams;


### Math and Date Functions
- CAST(): The CAST() function is used to convert the value of an expression into another data type.
SELECT CAST(expr AS type-name);
SELECT CAST(3 AS REAL) / 2; -- 1.5
SELECT CAST('3.14 is pi' AS REAL);

- DATE and DATETIME functions:
SELECT DATETIME('2020-09-01 17:38:22');
SELECT DATETIME('now');
SELECT DATETIME('now', 'localtime');
SELECT TIME('2020-09-01 17:38:22'); -- 17:38:22
SELECT DATE('2020-09-01 17:38:22'); -- 2020-09-01
SELECT DATETIME('2020-02-10', 'start of month', '-1 day', '+7 hours');

STRFTIME(format, timestring, modifier1, modifier2, ...)
SELECT STRFTIME('%m %Y', 'now');


### Usage Funnels
:how users progress through a series of steps or events toward a specific goal or conversion.

1. Defining the Funnel Steps
   1. Imagine an e-commerce site where users go through a three-step funnel: “View Product” ➡ “Add to Cart” ➡ “Checkout”.
   2. We’ll use an event table with the following schema:
   3. The funnel steps are defined by:
        Users who have performed a particular event (e.g., “View Product”).
        The event performed within a specific time frame (e.g., since September 2017).
2. Constructing the Funnel Steps: We’ll build the funnel steps as three successive queries:
   1. Step 1: Distinct users who’ve viewed any product since September 2017:
    SELECT DISTINCT user_id
    FROM events
    WHERE event = 'View Product'
        AND timestamp BETWEEN '2017-09-01'::timestamp AND NOW();
   2. Step 2: Users who’ve added products to the cart within 7 days of viewing a product:
    SELECT DISTINCT user_id
    FROM events s2
    INNER JOIN (
        SELECT DISTINCT user_id
        FROM events
        WHERE event = 'View Product'
            AND timestamp BETWEEN '2017-09-01'::timestamp AND NOW()
    ) s1 ON s1.user_id = s2.user_id
    WHERE s2.timestamp < (s1.timestamp + '7 days'::interval)
        AND s2.event = 'Add to Cart';

   3. Improving the Funnel Over Time:
      - While basic funnel analysis is powerful, consider tracking how the funnel improves over time.
      - Quantify results from A/B testing, personnel changes, and process adjustments.
      - Present data as a pivoted table for clarity.

e.g.
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
SELECT browse_date,
   COUNT(*) AS 'num_browse',
   SUM(is_checkout) AS 'num_checkout',
   SUM(is_purchase) AS 'num_purchase',
   1.0 * SUM(is_checkout) / COUNT(user_id) AS 'browse_to_checkout',
   1.0 * SUM(is_purchase) / SUM(is_checkout) AS 'checkout_to_purchase'
FROM funnels
GROUP BY browse_date
ORDER BY browse_date;

### User Churn
WITH enrollments AS 
(SELECT *
FROM subscriptions
WHERE subscription_start < '2017-01-01'
AND 
  subscription_end >= '2017-01-01'
  OR subscription_end IS NULL
),
status AS 
(SELECT 
CASE
  WHEN subscription_end > '2017-01-31'
    OR subscription_end IS NULL THEN 0
  ELSE 1
  END as is_canceled,
CASE
  WHEN subscription_start < '2017-01-01'
    AND (
      subscription_end >= '2017-01-01'
        OR subscription_end IS NULL
    ) THEN 1
    ELSE 0
  END as is_active
FROM enrollments
)
SELECT 1.0 * SUM(is_canceled)/SUM(is_active) FROM status;

==SAME==
WITH enrollments AS 
(SELECT *
FROM subscriptions
WHERE subscription_start < '2017-01-01'
AND 
  subscription_end >= '2017-01-01'
  OR subscription_end IS NULL
),
status AS 
(SELECT 
CASE
  WHEN subscription_end BETWEEN '2017-01-01' AND '2017-01-31' THEN 1
  ELSE 0
  END as is_canceled,
CASE
  WHEN subscription_start < '2017-01-01'
    AND (
      subscription_end >= '2017-01-01'
        OR subscription_end IS NULL
    ) THEN 1
    ELSE 0
  END as is_active
FROM enrollments
)
SELECT 1.0 * SUM(is_canceled)/SUM(is_active) FROM status;

Create Months Temporary Table
WITH months as
(SELECT
  '2017-01-01' as first_day,
  '2017-01-31' as last_day
UNION
SELECT
  '2017-02-01' as first_day,
  '2017-02-28' as last_day
UNION
SELECT
  '2017-03-01' as first_day,
  '2017-03-31' as last_day
)
SELECT *
FROM months;

+ Cross Join
cross_join AS
(SELECT *
FROM subscriptions
CROSS JOIN months)
SELECT *
FROM cross_join
LIMIT 100;

**To get active users and canceled users in certain periods(by months)**
WITH months AS
(SELECT
  '2017-01-01' as first_day,
  '2017-01-31' as last_day
UNION
SELECT
  '2017-02-01' as first_day,
  '2017-02-28' as last_day
UNION
SELECT
  '2017-03-01' as first_day,
  '2017-03-31' as last_day
),
cross_join AS
(SELECT *
FROM subscriptions
CROSS JOIN months),
status AS
(SELECT id, first_day as month,
CASE
  WHEN (subscription_start < first_day)
    AND (
      subscription_end > first_day
      OR subscription_end IS NULL
    ) THEN 1
  ELSE 0
END as is_active,
CASE 
  WHEN subscription_end BETWEEN first_day AND last_day THEN 1
  ELSE 0
END as is_canceled
FROM cross_join),
status_aggregate AS
(SELECT
  month,
  SUM(is_active) as active,
  SUM(is_canceled) as canceled
FROM status
GROUP BY month)
SELECT *
FROM status_aggregate;

**To get chrun rates in certain periods(by months)**
WITH months AS
(SELECT
  '2017-01-01' as first_day,
  '2017-01-31' as last_day
UNION
SELECT
  '2017-02-01' as first_day,
  '2017-02-28' as last_day
UNION
SELECT
  '2017-03-01' as first_day,
  '2017-03-31' as last_day
),
cross_join AS
(SELECT *
FROM subscriptions
CROSS JOIN months),
status AS
(SELECT id, first_day as month,
CASE
  WHEN (subscription_start < first_day)
    AND (
      subscription_end > first_day
      OR subscription_end IS NULL
    ) THEN 1
  ELSE 0
END as is_active,
CASE 
  WHEN subscription_end BETWEEN first_day AND last_day THEN 1
  ELSE 0
END as is_canceled
FROM cross_join),
status_aggregate AS
(SELECT
  month,
  SUM(is_active) as active,
  SUM(is_canceled) as canceled
FROM status
GROUP BY month)
SELECT
  month,
  1.0 * canceled/active AS churn_rate
FROM status_aggregate;


### Attribution Query
WITH last_touch AS (
    SELECT user_id,
       MAX(timestamp) AS 'last_touch_at'
    FROM page_visits
    GROUP BY user_id)
SELECT lt.user_id,
   lt.last_touch_at,
   pv.utm_source
FROM last_touch AS 'lt'
JOIN page_visits AS 'pv'
   ON lt.user_id = pv.user_id
   AND lt.last_touch_at = pv.timestamp
WHERE lt.user_id = 10069;