# Uge5 Product and Transaction system

## Diagrams

### First draft diagram
Original and first draft of the project. Here i imagined the code could be used in a front-end product-sale-website.
Initially I had multiple factories. Now I just have 1 for all the types.
![First draft of project](diagrams/flowchart_draft_1.png)

### Pyreverse diagrams
Here are the pyreverse generated diagrams
Class diagram
![Pyreverse_classes](diagrams/classes_Uge5.png)
Packages diagram
![Pyreverse_packages](diagrams/packages_Uge5.png)


## Installation

1. Create environment:
    ```
    python -m venv .venv
    ```

2. Activate environment:
    ```
    .venv\Scripts\activate
    ```

3. Install requirements:
    ```
    pip install -r requirements.txt
    ```

4. Run the tests
    make sure you're in /code/
    ```
    python -m unittest newTest.py
    ```