# %%
import statsmodels.api as sm

y = [1, 2, 3, 4, 5]
X = range(1, 6)
X = sm.add_constant(X)

model = sm.OLS(y, X)
results = model.fit()
print(results.summary())