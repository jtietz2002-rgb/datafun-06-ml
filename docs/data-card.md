# Data Card: Student Data

This Data Card documents the dataset used by the
`student_gpa_act_data` experiment.

It follows the general transparency goals of Google's
Data Cards Playbook:
describe dataset provenance, composition,
intended use, limitations, and considerations
not apparent from the data.

## Dataset Summary

| Item                                | Description                    |
| ----------------------------------- | ------------------------------ |
| Dataset                             | Student Data                   |
| Curated dataset                     | `student_gpa_act_data          |
| Observations                        | 100 students                   |
| High school GPA                     | Range 0-4.0                    |
| ACT score                           | Range 0-36                     |
| College GPA                         | Range 0-4.0                    |
| Grain                               | one student                    |
| Primary use here                    | supervised regression          |
| Target in this experiment           | `CollegeGPA_Year1`                  |
| Selected feature in this experiment | `ACTScore`            |

## Purpose and Provenance

This is an AI-generated dataset for the purpose of practicing regression modeling.


## Dataset Composition

The dataset contains 100 observations representing individual students.

The variables available through the Seaborn version used in this project are:

- `CollegeGPA_Year1`
- `ACTScore`
- `HighSchoolGPA`
- `StudentID`
-

For this experiment, only two columns are required:

- `CollegeGPA_Year1`
- `ACTScore`

## Intended Use

The dataset is appropriate for:

- education
- exploratory data analysis
- visualization
- introductory statistical analysis
- supervised machine-learning experiments
- demonstrating reproducible analytical workflows

In this repository, the dataset is used to demonstrate a clear
baseline-versus-candidate regression experiment.

## Additional Exploration

Other reasonable analytical questions include:

- using High School GPA to predict College GPA
- using High School GPA to predict ACT score
- using both High School GPA and ACT score to predict College GPA

Those are separate analytical experiments and should have their own
declared assumptions, selected features, evaluation methods, and conclusions.

## Limitations

The dataset is very small and is not based on actual students.

Results should therefore not automatically be generalized to:

- real students


A predictive relationship observed in this dataset should not be interpreted
automatically as a causal relationship.


## Project Data Processing

The project:

1. loads the student information dataset
2. observes the available columns
3. validates the selected feature and target
4. selects `CollegeGPA_Year1` and `ACTScore`
5. drops observations missing either required value
6. performs the declared train/test experiment


---

[◄ Back to Home](index.md)
