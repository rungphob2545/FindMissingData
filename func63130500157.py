def fillna_global_mean(df,col_im):
    m = df[col_im].mean()
    df[col_im] = df[col_im].fillna(m)
    return df
def fillna_group_mean(df,col_im,_col_gr):
    for g in df[col_gr].unique():
        m = df[col_im][df[col_gr]==g].mean()
        df[col_im][df[col_gr]==g] = df[col_im][df[col_gr]==g].fillna(m)
    return df
def fillna_global_mode(df,col_im):
    m = df[col_im].mode()[0]
    df[col_im] = df[col_im].fillna(m)
    return df
def fillna_group_mode(df,col_im,col_gr):
    for g in df[col_gr].unique():
        m = df[col_im][df[col_gr]==g].mode()
        df[col_im][df[col_gr]==g] = df[col_im][df[col_gr]==g].fillna(m)
    return df
def fillna_knn(df,k):
    #Homework Do something ...
    imputer = KNNImputer(n_neighbors=k)
    imputer.fit(df)
    df = imputer.transform(df)
    return df
### READ DATE