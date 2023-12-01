#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#| label: 08-hitters-dataset
#| echo: false
library(dplyr)
library(tidyr)
library(readr)

df <- read_csv('./data/Hitters.csv') %>% 
select(Names, Hits, Years, Salary) %>% 
drop_na() %>% 
mutate(log_Salary = log(Salary))

df
#
#
#
#| label: 08-reg-trees-intro
#| echo: false
#| out-width: 100%
knitr::include_graphics("images/08_1_salary_data.png")

knitr::include_graphics("images/08_2_basic_tree.png")
#
#
#
#
#
#
#
#
#
#
#| label: 08-decision-trees-terminology-1
#| echo: false
#| out-width: 100%
knitr::include_graphics("images/08_3_basic_tree_term.png")
#
#
#
#| label: 08-decision-trees-terminology-2
#| echo: false
#| fig-cap: The three-region partition for the Hitters data set from the regression tree
#| out-width: 100%
knitr::include_graphics("images/08_4_hitters_predictor_space.png")
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#| label: 08-reg-trees-interpreration
#| echo: false
#| out-width: 100%
knitr::include_graphics("images/08_2_basic_tree.png")
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#| label: 08-purning-a-tree
#| echo: false
#| out-width: 100%
knitr::include_graphics("images/08_5_hitters_unpruned_tree.png")
#
#
#
#| label: 08-mse-cross-validation
#| echo: false
#| out-width: 100%
#| fig-cap: 'Training, cross-validation, and test MSE are shown as a function of the number of terminal nodes in the pruned tree. Standard error bands are displayed. The minimum cross-validation error occurs at a tree size of 3.'
knitr::include_graphics("images/08_6_hitters_mse.png")
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#| label: 08-heart-dataet-cross-valudation
#| echo: false
#| out-width: 100%
#| fig-cap: 'Heart data. Top: The unpruned tree. Bottom Left: Cross-validation error, training, and test error, for different sizes of the pruned tree. Bottom Right: The pruned tree corresponding to the minimal cross-validation error.'
knitr::include_graphics("images/08_7_classif_tree_heart.png")
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#| label: 08-variable-importance
#| echo: false
#| out-width: 100%
#| fig-cap: 'A variable importance plot for the Heart data. Variable importance is computed using the mean decrease in Gini index, and expressed relative to the maximum.'
knitr::include_graphics("images/08_8_var_importance.png")
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#| label: 08-random-forest
#| echo: false
#| out-width: 100%
#| fig-cap: 'Results from random forests for the 15-class gene expression data set with p = 500 predictors. The test error is displayed as a function of the number of trees. Random forests (m < p) lead to a slight improvement over bagging (m = p). A single classification tree has an error rate of 45.7%.'
knitr::include_graphics("images/08_9_rand_forest_gene_exp.png")
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#| label: 08-boosting-algo
#| echo: false
#| out-width: 100%
knitr::include_graphics("images/08_10_boosting_algorithm.png")
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#| label: 08-boosting-vs-rf
#| echo: false
#| out-width: 100%
#| fig-cap: 'Results from performing boosting and random forests on the 15-class gene expression data set in order to predict cancer versus normal. The test error is displayed as a function of the number of trees. For the two boosted models, lambda = 0.01. Depth-1 trees slightly outperform depth-2 trees, and both outperform the random forest, although the standard errors are around 0.02, making none of these differences significant. The test error rate for a single tree is 24 %.'
knitr::include_graphics("images/08_11_boosting_gene_exp_data.png")
#
#
#
#
#
#
#
#
#
#
#
#
