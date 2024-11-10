from typing import list, List, Tuple, Optional
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split

class DataProcessing:
    '''
    Process raw data and convert it into train, val, and test sets.
    '''
    def __init__(self, 
            train_data_path: str,
            test_data_path: str,
            id_cols: list, 
            numerical_data_cols: list, 
            catergorical_data_cols: list,
            target_variable: list,
            test_split_ratio: int = 0.2
        ):
        self.train_data_path = train_data_path
        self.test_data_path = test_data_path
        self.id_cols = id_cols
        self.numerical_data_cols = numerical_data_cols
        self.catergorical_data_cols = catergorical_data_cols
        self.target_variable = target_variable
        self.test_split_ratio = test_split_ratio

    def __file_loader__(self, test: bool = True) -> pd.DataFrame:
        if test==False:
            data = pd.read_csv(self.train_data_path)
            return data
        else:
            test_data = pd.read_csv(self.test_data_path)
            return test_data

    def __splitter__(self, X: pd.DataFrame, y: pd.DataFrame) -> Tuple[pd.DataFrame]:
        X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=self.test_split_ratio)
        return (X_train, X_val, y_train, y_val)
    
    def __id_processor__(self, X: List[pd.DataFrame]) -> Tuple[pd.DataFrame]:
        for _ in range(len(X)):
            x = X[_]
            X[_] = x["id"]
        return Tuple(X)

    def __numerical_data_processor__(self, X: List[pd.DataFrame]) -> Tuple[pd.DataFrame]:
        for _ in range(len(X)):
            x = X[_]
            X[_] = x[self.numerical_data_cols]
        
        sc = StandardScaler()
        X[0] = sc.fit_transform(X[0])
        for _ in range(1, len(X)):
            x = X[_]
            X[_] = x.transform(x)
        return tuple(X)
    
    def __categorical_data_processor__(self, X: List[pd.DataFrame]) -> Tuple[pd.DataFrame]:
        for _ in range(len(X)):
            x = X[_]
            X[_] = x[self.catergorical_data_cols]
        
        one_hot_encoder = OneHotEncoder(sparse_output=False)
        X[0] = one_hot_encoder.fit_transform(X[0])
        X[0] = pd.DataFrame(X[0], columns=one_hot_encoder.get_feature_names_out(self.catergorical_data_cols))
        for _ in range(1, len(X)):
            x = X[_]
            X[_] = one_hot_encoder.transform(x)
            X[_] = pd.DataFrame(X[_], columns=one_hot_encoder.get_feature_names_out(self.catergorical_data_cols))
        return tuple(X)
    
    def __concatenate_data__(self, X_id: Tuple[pd.DataFrame], X_num: Tuple[pd.DataFrame], X_cat: Tuple[pd.DataFrame]) -> Optional[Tuple[pd.DataFrame]]:
        len_x_id, len_x_num, len_x_cat = len(X_id), len(X_num), len(X_cat)
        if len_x_id!=len_x_num or len_x_id!=len_x_cat or len_x_num!=len_x_cat:
            raise Exception(f"Input tuples are of uneven length. \nMake sure length of each tuple is equal to the lenght of the other tuples.")
        
        X = [None for _ in range(len_x_id)]
        for _ in range(len_x_id):
            X[_] = pd.concat([X_id[_], X_num[_], X_cat[_]], axis=1)

        return tuple(X)

    
    def data_processor(self) -> Tuple[Tuple[pd.DataFrame]]:
        main_data = self.__file_loader__(test=False)
        test_data = self.__file_loader__(test=True)

        y_main = main_data[self.target_variable]
        X_main = main_data.drop(self.target_variable, axis=1)

        try:
            y_test = test_data[self.target_variable]
            X_test = test_data.drop(self.target_variable, axis=1)
        except:
            y_test = None
            X_test = test_data

        (X_train, X_val, y_train, y_val) = self.__splitter__(X = X_main, y = y_main)
        X = (X_train, X_val, X_test)
        if y_test:
            y = (y_train, y_val, y_test)
        else:
            y = (y_train, y_val)

        X_id = self.__id_processor__(X)
        X_num = self.__numerical_data_processor__(X)
        X_cat = self.__categorical_data_processor__(X)

        X = self.__concatenate_data__(X_id=X_id, X_num=X_num, X_cat=X_cat)
        return (X, y)