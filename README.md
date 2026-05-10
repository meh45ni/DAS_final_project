# My Car Price Project

## What is this about?:

So, I made this project to see if we can know a car price before we buy it. I used a big list of 2,500 cars from Kaggle. It has things like mileage, year, and brand. My goal was to make a math model that guess the price so people don't get scammed.

## How I did it:
### 1. Cleaning the data

The data was a bit dirty at first.
  I removed Car ID and Model name because they just confuse the math.

  Most important: computers don't know what "Audi" or "Petrol" means. So I used get_dummies to turn those words into numbers (0 and 1). If I didn't do this, the code would just crash.

### 2. Looking at the charts (EDA)

I made some graphs to see the "vibe" of the data.

   I saw that when Mileage go up, the Price go down almost every time.

   This prove that Linear Regression is the right tool for this job because the relationship is clear.

### 3. Modeling

I used the Linear Regression from sklearn.

   I gave 80% of data to the model to learn. The other 20% I keep it secret to test if the model is smart or just lucky.

   My model got an R² score of -0.0038 which is not accurate at all. It's actually worse than just guessing

### 4. The Dashboard

For the final part, I used Streamlit (like we did in Lab 6).

   I put a checkbox to show the raw data.

   I put the graphs so it looks professional.

   And I added a slider. You can move it to change the mileage, and the app tell you the price immediately.

## How to run the code

If you want to run it, you need pandas, sklearn, and streamlit. Just open the terminal in this folder and write:

    python -m streamlit run app.py


## Conclusion:
This project taught me that data cleaning is 70% of the work. If the data is messy, the model gives bad results. I also saw that math has limits, my model can't know if a car had a crash or a broken engine, so the price is just a guess. Still, I’m happy I built a full pipeline and a working dashboard that shows how things like mileage change the price.
