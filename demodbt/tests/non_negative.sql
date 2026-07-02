{# a singular test #}

SELECT * FROM 
{{ ref('t_sales') }}
WHERE gross_amount < 0 AND net_amount < 0