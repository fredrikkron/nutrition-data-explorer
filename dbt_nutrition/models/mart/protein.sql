WITH protein AS (
    SELECT
        f.food_id,
        f.food_name,
        f.food_group,
        fn.value AS protein_amount
    FROM {{ ref('fct_food_nutrients') }} fn
    JOIN {{ ref('dim_food') }} f
        ON fn.food_id = f.food_id
    JOIN {{ ref('dim_nutrients') }} n
        ON fn.nutrient_id = n.nutrient_id
    WHERE n.nutrient_name = 'Protein'
),

selected_groups AS (
    SELECT *
    FROM protein
    WHERE food_group IN ('Baljväxter (bönor, linser och ärter)', 'Dessertost', 'Fisk färsk fryst kokt',
                        'Fisk o skaldjursprodukter o rätter', 'Fågel ', 'Hård ost mm', 'Inälvor och organ',
                        'Kött färskt fryst tillagat ', 'Kött processat', 'Nötter frön', 'Vegetabiliskt protein produkter och rätter')
),

ranked AS (
    SELECT
        food_id,
        food_name,
        food_group,
        protein_amount,
        ROW_NUMBER() OVER (PARTITION BY food_group ORDER BY protein_amount DESC) AS ranking
    FROM selected_groups
)

SELECT
    food_id,
    food_name,
    food_group,
    protein_amount
FROM ranked
WHERE ranking <= 10
ORDER BY food_group, protein_amount DESC