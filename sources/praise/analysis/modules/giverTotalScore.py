import plotly.express as px

header = "Praise Giving Distribution"
description = "We can also take a look at the distribution of the people giving praise."

def run(praise_distribution):
  #first we calculate the individual contributions of each praise giver
  praise_by_giver = praise_distribution[['FROM USER ACCOUNT', 'AVG SCORE', 'PERCENTAGE', 'TOKEN TO RECEIVE']].copy().groupby(['FROM USER ACCOUNT']).agg('sum').reset_index()
  praise_by_giver.rename(columns= {'TOKEN TO RECEIVE': 'TOKENS GAVE'}, inplace = True)
  praise_by_giver.sort_values(by='TOKENS GAVE',inplace=True,ascending=False)

  fig_praisegiver = px.bar(praise_by_giver, x="FROM USER ACCOUNT",y='TOKENS GAVE',title='Praise Giver Sorted by Total Score')
  fig_praisegiver.show()
