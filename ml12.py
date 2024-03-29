{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "#loading data via pandas\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sb\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "# loading data from URL and converting into dataframe\n",
    "df=pd.read_csv(\"bank.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 10000 entries, 0 to 9999\n",
      "Data columns (total 14 columns):\n",
      "RowNumber          10000 non-null int64\n",
      "CustomerId         10000 non-null int64\n",
      "Surname            10000 non-null object\n",
      "CreditScore        10000 non-null int64\n",
      "Geography          10000 non-null object\n",
      "Gender             10000 non-null object\n",
      "Age                10000 non-null int64\n",
      "Tenure             10000 non-null int64\n",
      "Balance            10000 non-null float64\n",
      "NumOfProducts      10000 non-null int64\n",
      "HasCrCard          10000 non-null int64\n",
      "IsActiveMember     10000 non-null int64\n",
      "EstimatedSalary    10000 non-null float64\n",
      "Exited             10000 non-null int64\n",
      "dtypes: float64(2), int64(9), object(3)\n",
      "memory usage: 1.1+ MB\n"
     ]
    }
   ],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>RowNumber</th>\n",
       "      <th>CustomerId</th>\n",
       "      <th>Surname</th>\n",
       "      <th>CreditScore</th>\n",
       "      <th>Geography</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Age</th>\n",
       "      <th>Tenure</th>\n",
       "      <th>Balance</th>\n",
       "      <th>NumOfProducts</th>\n",
       "      <th>HasCrCard</th>\n",
       "      <th>IsActiveMember</th>\n",
       "      <th>EstimatedSalary</th>\n",
       "      <th>Exited</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>15634602</td>\n",
       "      <td>Hargrave</td>\n",
       "      <td>619</td>\n",
       "      <td>France</td>\n",
       "      <td>Female</td>\n",
       "      <td>42</td>\n",
       "      <td>2</td>\n",
       "      <td>0.00</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>101348.88</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>15647311</td>\n",
       "      <td>Hill</td>\n",
       "      <td>608</td>\n",
       "      <td>Spain</td>\n",
       "      <td>Female</td>\n",
       "      <td>41</td>\n",
       "      <td>1</td>\n",
       "      <td>83807.86</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>112542.58</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>15619304</td>\n",
       "      <td>Onio</td>\n",
       "      <td>502</td>\n",
       "      <td>France</td>\n",
       "      <td>Female</td>\n",
       "      <td>42</td>\n",
       "      <td>8</td>\n",
       "      <td>159660.80</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>113931.57</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>15701354</td>\n",
       "      <td>Boni</td>\n",
       "      <td>699</td>\n",
       "      <td>France</td>\n",
       "      <td>Female</td>\n",
       "      <td>39</td>\n",
       "      <td>1</td>\n",
       "      <td>0.00</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>93826.63</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>15737888</td>\n",
       "      <td>Mitchell</td>\n",
       "      <td>850</td>\n",
       "      <td>Spain</td>\n",
       "      <td>Female</td>\n",
       "      <td>43</td>\n",
       "      <td>2</td>\n",
       "      <td>125510.82</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>79084.10</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   RowNumber  CustomerId   Surname  CreditScore Geography  Gender  Age  \\\n",
       "0          1    15634602  Hargrave          619    France  Female   42   \n",
       "1          2    15647311      Hill          608     Spain  Female   41   \n",
       "2          3    15619304      Onio          502    France  Female   42   \n",
       "3          4    15701354      Boni          699    France  Female   39   \n",
       "4          5    15737888  Mitchell          850     Spain  Female   43   \n",
       "\n",
       "   Tenure    Balance  NumOfProducts  HasCrCard  IsActiveMember  \\\n",
       "0       2       0.00              1          1               1   \n",
       "1       1   83807.86              1          0               1   \n",
       "2       8  159660.80              3          1               0   \n",
       "3       1       0.00              2          0               0   \n",
       "4       2  125510.82              1          1               1   \n",
       "\n",
       "   EstimatedSalary  Exited  \n",
       "0        101348.88       1  \n",
       "1        112542.58       0  \n",
       "2        113931.57       1  \n",
       "3         93826.63       0  \n",
       "4         79084.10       0  "
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# top 5 lines\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x7f08a1ec3668>"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# countplot by seaborn\n",
    "sb.countplot(df[\"Gender\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x7f089fe5cf98>"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sb.countplot(df[\"Geography\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[<matplotlib.axes._subplots.AxesSubplot object at 0x7f089f77cef0>,\n",
       "        <matplotlib.axes._subplots.AxesSubplot object at 0x7f089f725ef0>,\n",
       "        <matplotlib.axes._subplots.AxesSubplot object at 0x7f089f6e24e0>],\n",
       "       [<matplotlib.axes._subplots.AxesSubplot object at 0x7f089f690a90>,\n",
       "        <matplotlib.axes._subplots.AxesSubplot object at 0x7f089f6ce080>,\n",
       "        <matplotlib.axes._subplots.AxesSubplot object at 0x7f089f67f630>],\n",
       "       [<matplotlib.axes._subplots.AxesSubplot object at 0x7f089f62fbe0>,\n",
       "        <matplotlib.axes._subplots.AxesSubplot object at 0x7f089f5ee208>,\n",
       "        <matplotlib.axes._subplots.AxesSubplot object at 0x7f089f5ee240>],\n",
       "       [<matplotlib.axes._subplots.AxesSubplot object at 0x7f089f550d30>,\n",
       "        <matplotlib.axes._subplots.AxesSubplot object at 0x7f089f50f2e8>,\n",
       "        <matplotlib.axes._subplots.AxesSubplot object at 0x7f089f53e898>]],\n",
       "      dtype=object)"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 720x1080 with 12 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#histogram\n",
    "df.hist(figsize=(10,15))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "# features and label of data\n",
    "features=df.iloc[0:,3:13].values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[619, 'France', 'Female', ..., 1, 1, 101348.88],\n",
       "       [608, 'Spain', 'Female', ..., 0, 1, 112542.58],\n",
       "       [502, 'France', 'Female', ..., 1, 0, 113931.57],\n",
       "       ...,\n",
       "       [709, 'France', 'Female', ..., 0, 1, 42085.58],\n",
       "       [772, 'Germany', 'Male', ..., 1, 0, 92888.52],\n",
       "       [792, 'France', 'Female', ..., 1, 0, 38190.78]], dtype=object)"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "features"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "# bank exit status that is lable\n",
    "label=df.iloc[:,13].values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([1, 0, 1, ..., 1, 1, 0])"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "label"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "# to convert string data into numeric we can apply label encoding\n",
    "from sklearn.preprocessing import LabelEncoder\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "countenc=LabelEncoder()   # function call"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [],
   "source": [
    "features[0:,1]=countenc.fit_transform(features[0:,1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[619, 0, 'Female', ..., 1, 1, 101348.88],\n",
       "       [608, 2, 'Female', ..., 0, 1, 112542.58],\n",
       "       [502, 0, 'Female', ..., 1, 0, 113931.57],\n",
       "       ...,\n",
       "       [709, 0, 'Female', ..., 0, 1, 42085.58],\n",
       "       [772, 1, 'Male', ..., 1, 0, 92888.52],\n",
       "       [792, 0, 'Female', ..., 1, 0, 38190.78]], dtype=object)"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "features\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [],
   "source": [
    "# same for gender\n",
    "features[0:,2]=countenc.fit_transform(features[0:,2])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[619, 0, 0, ..., 1, 1, 101348.88],\n",
       "       [608, 2, 0, ..., 0, 1, 112542.58],\n",
       "       [502, 0, 0, ..., 1, 0, 113931.57],\n",
       "       ...,\n",
       "       [709, 0, 0, ..., 0, 1, 42085.58],\n",
       "       [772, 1, 1, ..., 1, 0, 92888.52],\n",
       "       [792, 0, 0, ..., 1, 0, 38190.78]], dtype=object)"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "features"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [],
   "source": [
    "# creating dummy variable using OneHot encoder\n",
    "from sklearn.preprocessing import OneHotEncoder"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [],
   "source": [
    "# calling function\n",
    "counthot=OneHotEncoder(categorical_features=[1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/home/deepanshu/.local/lib/python3.6/site-packages/sklearn/preprocessing/_encoders.py:415: FutureWarning: The handling of integer data will change in version 0.22. Currently, the categories are determined based on the range [0, max(values)], while in the future they will be determined based on the unique values.\n",
      "If you want the future behaviour and silence this warning, you can specify \"categories='auto'\".\n",
      "In case you used a LabelEncoder before this OneHotEncoder to convert the categories to integers, then you can now use the OneHotEncoder directly.\n",
      "  warnings.warn(msg, FutureWarning)\n",
      "/home/deepanshu/.local/lib/python3.6/site-packages/sklearn/preprocessing/_encoders.py:451: DeprecationWarning: The 'categorical_features' keyword is deprecated in version 0.20 and will be removed in 0.22. You can use the ColumnTransformer instead.\n",
      "  \"use the ColumnTransformer instead.\", DeprecationWarning)\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "array([[1.0000000e+00, 0.0000000e+00, 0.0000000e+00, ..., 1.0000000e+00,\n",
       "        1.0000000e+00, 1.0134888e+05],\n",
       "       [0.0000000e+00, 0.0000000e+00, 1.0000000e+00, ..., 0.0000000e+00,\n",
       "        1.0000000e+00, 1.1254258e+05],\n",
       "       [1.0000000e+00, 0.0000000e+00, 0.0000000e+00, ..., 1.0000000e+00,\n",
       "        0.0000000e+00, 1.1393157e+05],\n",
       "       ...,\n",
       "       [1.0000000e+00, 0.0000000e+00, 0.0000000e+00, ..., 0.0000000e+00,\n",
       "        1.0000000e+00, 4.2085580e+04],\n",
       "       [0.0000000e+00, 1.0000000e+00, 0.0000000e+00, ..., 1.0000000e+00,\n",
       "        0.0000000e+00, 9.2888520e+04],\n",
       "       [1.0000000e+00, 0.0000000e+00, 0.0000000e+00, ..., 1.0000000e+00,\n",
       "        0.0000000e+00, 3.8190780e+04]])"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# fit and transform\n",
    "counthot.fit_transform(features).toarray()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# training and testing\n",
    "# feature scalling"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
