import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df=pd.read_csv("data.csv", delimiter="\t")

# Identify missing values and duplicates
print("Missing values: ", df.isnull().sum())
print("Number of duplicates: ", df.duplicated().sum())

# Handle missing values by filling with the avg 
df["reviews_per_month"].fillna(df["reviews_per_month"].mean(), inplace=True)
df["price"].fillna(df["price"].mean(), inplace=True)
df["number_of_reviews"].fillna(df["number_of_reviews"].mean(), inplace=True)

# Drop rows where data is still missing and duplicates
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

# After the initial Cleaning
# print(df.head())
# print(df.info())
# print("Shape",df.shape)
# print(df.describe())


# Data visualization
df["price"].plot()
plt.ylabel("Price")
plt.title("Plot of prices")
# plt.show()

df.plot(kind="scatter", x="price", y="number_of_reviews", color="purple")
plt.title("Price vs Number of reviews")
# plt.show()

# Power of subplots
fig, axs = plt.subplots(2,3,figsize=(15,10))

# Price vs. Freq
axs[0,0].hist(df['price'], bins=20, color='lightblue')
axs[0,0].set_title("Price vs frequency")
axs[0,0].set_xlabel("Price")
axs[0,0].set_ylabel("Frequency")

# Number of reviews vs Frequency
axs[0,1].hist(df['number_of_reviews'], bins=20, color='red')
axs[0,1].set_title("Number_of_reviews vs Frequency")
axs[0,1].set_xlabel("number_of_reviews")
axs[0,1].set_ylabel("Frequency")

# Group by type of room and show avg price
room_type = df.groupby(by='room_type')['price'].mean().reset_index()
axs[0,2].bar(room_type['room_type'],room_type['price'],color='lightgreen')
axs[0,2].set_title("Avg price by room type")
axs[0,2].set_xlabel("Room Type")
axs[0,2].set_ylabel("Price")

# Number of listings in each borough (NYC)
neighborhoods = df['neighbourhood_group'].value_counts().reset_index()
neighborhoods.columns = ['neighbourhood_group', 'count']

axs[1,0].bar(neighborhoods["neighbourhood_group"], neighborhoods['count'], color="orange")
axs[1,0].set_title("Listings by Neighborhood")
axs[1,0].set_xlabel("Neighborhood")
axs[1,0].set_ylabel("Number of Listings")

# Price vs number of reviews
axs[1,1].scatter(df['price'], df['number_of_reviews'], color='blue')
axs[1,1].set_title("Price by Reviews")
axs[1,1].set_xlabel("Price")
axs[1,1].set_ylabel("Number of Reviews")

plt.tight_layout()
plt.show()
