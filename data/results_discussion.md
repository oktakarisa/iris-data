
# Problem 8: Discussion of Results

After looking at the plots and correlations, here are the main insights:

- **Setosa**: This species is the easiest to recognize. Its petals are short and narrow compared to the others, so it stands apart very clearly in both scatter plots and box/violin plots.

- **Versicolor vs. Virginica**: These two are more alike. Their measurements overlap, especially in the petal features. You can still separate them to some degree, but it is not as sharp as with Setosa.

- **Sepal features**: Sepal length and width do not do a great job at separating the three species. Their ranges often overlap, so they are less useful for classification on their own.

- **Correlations**: Petal length and petal width rise and fall together — a strong link shows up in the correlation matrix and heatmap. Sepal width, however, does not strongly connect with the other features.

**Takeaway**: Petal size (length and width) gives the clearest signal for telling species apart. Setosa is easy to spot, while Versicolor and Virginica need closer attention since they share overlapping ranges.
