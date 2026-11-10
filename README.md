# Lily-Devops-Inclass-Activity

## Assignment Overview

This repository is to be used in my submission for **In-Class Activity #3: Building An Automated CI Pipeline Using Jenkins and Github**, offered through Virginia Commonwealth University for CMSC 426: Software as a Service.

The goal of this assignment is to implement a **Continuous Integartion (CI)** workflow using **Jenkins** in order to auomate the building and testing of a small python application stored in GitHub. This involves configuring a Jenkins Freestyle project, connecting Jenkins to this GitHub repository, executing automated build and test commands, configuring build triggers, interpreting console output, troubleshooting failed builds, and applying basic security protocols when integrating services.

By completing these objectives, I aim to develop a stronger understanding of **Continuous Integration**, its relationship to **DevOps**, and how automated workflows contribute to more reliable and maintable software development.

## Repository Structure

The repository is organized as follow:

- `./app.py` - Contains the primary Python application and the `add_numbers()` function used to demonstrate application functionality and automated testing.
- `./tests/` - Contains `test_app.py`, which implements automated unit tests using Python's built-in **unittest** framework. These tests verify the expected behavior of the app and allow Jenkins to identify successful or failed builds.
- `/README.md` - Provides an overview of the assignment, repository organization, required technologies, execution instructions, and CI workflow.
- `./.gitignore` - Specifies files and directories that should not be tracked by Git, including Python-generated cache files and other local artifacts. 

## Tech Stack

### Application & Testing

#### Python 3
    Programming language used to implement the sample application and its associated test cases.

#### unittest
    Python's built-in unit testing framework, used to define, execute, and evaluate automated tests without requiring additional testing libraries.

### Continuous Integration and Version Control

#### Git
    Version control system used to track changes to the application's source code, tests, and documentation.

#### GitHub
    Remote repository hosting service used to store the project and provide Jenkins with access to the latest committed source code.

#### Jenkins
    Automation server used to implement the Continuous Integration workflow. Jenkins will retrieve the repository, execute build and test commands, and report the results of each build.

### Development Environment

#### Visual Studio Code
    Code editor used to develop, organize, and maintain the application and its automated tests.

#### Windows 11
    Operating system used for local development and hosting the Jenkins automation server.

#### Eclipse Temurin JDK 21
    Java Development Kit used to support the Jenkins runtime environment.

## Prerequisites

Before attempting to run the application or execute the automated tests, please ensure that the following requirements have been satisfied:

- **Python 3** is installed and accessible through the system's PATH.
- **Git** is installed for cloning and maintaining the repository.
- **Jenkins** is installed and configured if the Continuous Integration workflow will be executed.

Note that Jenkins is **not** required to run the application or its tests locally.

## How to Run the Application

Assuming the prerequisites have been met, the sample application can be executed directly through Python.

1. Clone this repository to your local machine using Git or GitHub CLI.
2. Open the cloned repository in Visual Studio Code or your preferred development environment.
3. Open a terminal and navigate to the repository's root directory, where `app.py` is located.
4. Verify that Python is installed by running:
    `python --version`
5. Execute the application:
    `python app.py`
6. The application should produce the following output:
    ```
    All systems go! Application started!
    2 + 3 = 5
    ```
This confirms that the sample application has executed successfully.

## How to Run the Automated Tests

The project's automated tests use Python's built-in unittest framework and do not require any additional dependencies.

1. Open the cloned repository in your chosen development environment (if you haven't already).
2. Open a terminal and navigate to the repository's root directory.
3. Execute the automated testing suite using the following command:
    `python -m unittest discover -s tests -v`
4. Python will discover the test cases located in the tests directory, execute each test, and compare the actual results against their expected values.
5. If both test cases pass, the terminal should display a summary similar to:
    ```
    Ran 2 tests

    OK
    ```
6. If a test fails, the framework will report the failed assertion and provide additional informaiton to help identify the problem.

These same automated tests will be incorporated into the Jenkins Continuous Integration workflow.

## CI Workflow

This project, as previously mentioned, is intended to demonstrate how Jenkins can automate the integration and testing of changes submitted to a GitHub repository.

The planned workflow consists of the following stages:

1. Source Code Management: Application source code and auotmated tests are maintained in the GitHub repository.
2. Build Trigger: A GitHub webhook notifies Jenkins when a build should begin.
3. Repository Checkout: Jenkins retrieves the latest version of the source code from GitHub.
4. Build Preparation: Jenkins executes the configurated preparation commands and verifies that the required project files are available.
5. Automated Testing: Jenkins runs the Python unit test suite and evaluates the results.
6. Build Reporting: Jenkins records the console output and marks the build as either successful or failed based on the results of the tests.

Once configured, this workflow will be tested using successful builds, intentional test failures, and recovery builds to demonstrate that Jenkins correctly detects and reports changes in application behavior.

## Security Considerations

The Jenkins installation uses a dedicated Windows service account, rather than a highly privledged LocalSystem account.

Jenkins authentication and repository permissions are configured to limit unnecessary access. Credentials, access token, and other sensitive configuration values should **not** be committed to this repository.

Any publicly accessible Jenkins integration should use appropriate authentication and encrypted HTTPS communication.

Additional security configuration and evaluation details are documented in my technical report. 