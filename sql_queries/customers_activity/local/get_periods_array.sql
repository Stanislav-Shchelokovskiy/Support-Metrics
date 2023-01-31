WITH RECURSIVE periods({start}, {period}) AS (
  VALUES({anchor_expr}, {anchor_expr_formatted})
  UNION ALL
  SELECT {recursive_expr}, {recursive_expr_formatted}
  FROM periods
  WHERE {recursion_cond_expr}
)
SELECT * FROM periods