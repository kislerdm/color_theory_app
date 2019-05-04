# Color Theory <a href="http://color-theory-app.s3-website-eu-west-1.amazonaws.com" target="_blank">App</a>

## Description

A toy project/demo on how to structure and develop micro-service driven application powered by machine learning service.

## App Idea

The app objective is to define **binary category** of a color selected by user. Two possible categories being *warm* and *cool* are <a href="https://en.wikipedia.org/wiki/Color_theory#Warm_vs._cool_colors" target="_blank">described</a> as following:

> Color theory has described perceptual and psychological effects to this contrast. Warm colors are said to advance or appear more active in a painting, while cool colors tend to recede; used in interior design or fashion, warm colors are said to arouse or stimulate the viewer, while cool colors calm and relax.

## App Structure

```
color_theory_app
    ├── backend
    └── frontend
```

The app has two service sides, frontend and backend:

- *frontend* can be generalised as the product with software engineers + DevOps maintaining and developing it
- *backend* can be generalised as the micro-service with data scientist/engineers/machine learning engineers + Dev-/DataOps maintaining and developing it

### Backend

#### Machine Learning Model Development

```
backend
  └── ml
      ├── data
      │   └── warm_cold_colors.csv
      ├── model
      │   └── model_v1.xgb
      └── model.ipynb
```

The models can be *iteratively* developed by the data scientists according to the flow:

```
consume data from data dir -> model training and evaluate service (model.ipynb) -> model export into model dir
```

#### API Service

Backend has the interface(s) to communicate with other services (fronted service in our case) with a set of end-points. It's usually being developed by data scientists, engineers, or machine learning engineers.

```
backend
  ├── Dockerfile
  ├── launch_api.sh
  └── api
       ├── ml_model
       ├── requirements.txt
       └── run_server.py      
```

API service uses the module **ml_model** with end-points definition and the service to make prediction on frontend request using the model from `./backend/ml/model/`.

The backend service is being launched by

```bash
sh launch_api.sh
```

### Frontend

Frontend service of the app gives a user the web interface to select a color of interest and define its category by communicating with the backend via its API end-point(s).

#### App Screenshot

![App Screen](fig/app_screen.png)

## Run the app

### Requirements

```bash
docker ver. >= 18.09
```

## App Launch

To launch the app, clone the repo

```bash
git clone git@github.com:kislerdm/color_theory_app.git && cd color_theory_app
```

and run the launch script

```bash
sh launch_services.sh
```
