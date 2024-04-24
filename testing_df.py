# # We will impute the missing values using an uniform distribution with parameters 
# # a=10 and b=14, as shown below:

# item_weight_indices_to_be_updated = train_df[train_df['Item_Weight'].isnull()].index
# ​
# train_df.loc[item_weight_indices_to_be_updated, 'Item_Weight'] = np.random.uniform(
#                                           10, 14, len(item_weight_indices_to_be_updated))
                                                                                   
                                                                                   