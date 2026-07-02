WITH

sales AS (
    SELECT
        sales_id,
        product_sk,
        customer_sk,
        gross_amount,
        payment_method
    FROM {{ ref('t_sales') }}
),

products AS (
    SELECT
        product_sk,
        category
    FROM
        {{ ref('t_product') }}
),

customers AS (
    SELECT
        customer_sk,
        gender
    FROM {{ ref('t_customer') }}
),

joined_data AS (
    SELECT
        sales.sales_id,
        sales.gross_amount,
        sales.payment_method,
        products.category,
        customers.gender
    FROM sales
    JOIN 
        products ON sales.product_sk = products.product_sk
    JOIN 
        customers ON sales.customer_sk = customers.customer_sk
)

SELECT
    category,
    gender,
    SUM(gross_amount) AS total_sales
FROM joined_data
GROUP BY category, gender
ORDER BY total_sales DESC




