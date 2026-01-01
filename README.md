# Geeks-For-Geeks — Curated Algorithms & Data Structures

[![Repo Size](https://img.shields.io/github/repo-size/mdzaheerjk/Geeks-For-Geeks)](https://github.com/mdzaheerjk/Geeks-For-Geeks)
[![Last Commit](https://img.shields.io/github/last-commit/mdzaheerjk/Geeks-For-Geeks)](https://github.com/mdzaheerjk/Geeks-For-Geeks/commits/main)
[![Issues](https://img.shields.io/github/issues/mdzaheerjk/Geeks-For-Geeks)](https://github.com/mdzaheerjk/Geeks-For-Geeks/issues)
[![License](https://img.shields.io/github/license/mdzaheerjk/Geeks-For-Geeks)](https://github.com/mdzaheerjk/Geeks-For-Geeks/blob/main/LICENSE)

A curated collection of algorithmic problems and solutions inspired by GeeksforGeeks — organized, tested, and implemented in multiple languages to help learning, interview prep, and reference.

---

Visual overview
---------------

<p align="center">
  <img alt="G4G-style" src="https://img.shields.io/badge/Geeks-For-Geeks-2ecc71?style=for-the-badge&logo=read-the-docs" />
</p>

Languages & tooling (logos)
---------------------------

<p align="center">
  <a href="#languages--tools"><img alt="Python" src="https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" /></a>
  <a href="#languages--tools"><img alt="C++" src="https://img.shields.io/badge/C%2B%2B-C%2B%2B17-00599C?style=for-the-badge&logo=c%2B%2B&logoColor=white" /></a>
  <a href="#languages--tools"><img alt="Java" src="https://img.shields.io/badge/Java-8%2B-007396?style=for-the-badge&logo=java&logoColor=white" /></a>
  <a href="#languages--tools"><img alt="JavaScript" src="https://img.shields.io/badge/JavaScript-ES6-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" /></a>
  <a href="#languages--tools"><img alt="Node.js" src="https://img.shields.io/badge/Node.js-16%2B-539E43?style=for-the-badge&logo=node.js&logoColor=white" /></a>
  <a href="#languages--tools"><img alt="CICD" src="https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white" /></a>
</p>

Table of Contents
- [About](#about)
- [What you'll find](#what-youll-find)
- [Languages & Tools](#languages--tools)
- [Quick Start](#quick-start)
  - [Python](#python)
  - [C++](#c)
  - [Java](#java)
  - [JavaScript / Node.js](#javascript--nodejs)
- [Repository Structure](#repository-structure)
- [How to use this repo](#how-to-use-this-repo)
- [Contribution Guidelines](#contribution-guidelines)
- [Code Style & Testing](#code-style--testing)
- [Pull Request Checklist](#pull-request-checklist)
- [License](#license)
- [Contact](#contact)

About
-----
This repository aims to:
- Provide clean, well-documented solutions to common algorithmic problems.
- Offer multi-language implementations where appropriate.
- Encourage community contributions with clear guidelines and a consistent structure.

What you'll find
----------------
- Problem statements (brief) with one-or-more solutions.
- Implementations in languages such as Python, C++, Java, JavaScript, and more.
- Example inputs/outputs and short explanations.
- (Optional) Unit tests or example runners where applicable.

Languages & Tools
-----------------
Primary languages typically include:
- ![Python logo](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white) Python 3.x
- ![C++ logo](https://img.shields.io/badge/-C%2B%2B-00599C?logo=c%2B%2B&logoColor=white) C++ (17/20)
- ![Java logo](https://img.shields.io/badge/-Java-007396?logo=java&logoColor=white) Java 8+
- ![JS logo](https://img.shields.io/badge/-JavaScript-F7DF1E?logo=javascript&logoColor=black) JavaScript (Node.js)

Tools & utilities:
- Formatting: Black (Python), clang-format (C++), prettier (JS), google-java-format (Java)
- Testing: pytest/unittest (Python), GoogleTest (C++)
- CI: GitHub Actions (add a workflow to run tests and format checks)

Quick Start
-----------

Clone the repo:
```bash
git clone https://github.com/mdzaheerjk/Geeks-For-Geeks.git
cd Geeks-For-Geeks
```

Python
- Run a single solution:
  ```bash
  python3 path/to/problem/solution.py
  ```
- (If present) install requirements:
  ```bash
  python3 -m pip install -r requirements.txt
  ```

C++
- Compile & run:
  ```bash
  g++ -std=c++17 path/to/problem/solution.cpp -O2 -o solution
  ./solution
  ```

Java
- Compile & run:
  ```bash
  javac path/to/problem/Solution.java
  java -cp path/to/problem Solution
  ```

JavaScript (Node.js)
- Run:
  ```bash
  node path/to/problem/solution.js
  ```

Repository Structure
--------------------
A recommended, consistent layout (actual layout may vary):

- /algorithms
  - /sorting
    - quick_sort/
      - README.md
      - solution.py
      - solution.cpp
      - test_quick_sort.py
  - /graphs
    - dijkstra/
- /data-structures
  - /trees
- /problems
  - problem-id-or-name/
    - statement.md
    - solution.py
    - solution.cpp
    - explanation.md
- /utils
  - helpers for testing and common code
- README.md
- CONTRIBUTING.md
- LICENSE

How to use this repo
--------------------
- Browse folders by topic (sorting, graphs, DP, etc.).
- Open a problem folder to read statement.md (if present) and solutions.
- Run the provided example or unit test to verify behavior.
- Use implementations as study/reference — restructure or port as needed.

Contribution Guidelines
-----------------------
Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a descriptive branch:
   - feature/<topic>-<short-desc>
   - fix/<problem-id>-<short-desc>
3. Add or update:
   - A problem folder with a brief `statement.md` (link to source if external).
   - One or more language implementations named consistently (e.g., solution.py, solution.cpp).
   - Brief `explanation.md` describing approach and complexity.
   - (Optional) Tests or example runner.
4. Follow code style and add comments explaining tricky parts.
5. Commit with clear messages and open a Pull Request to `main`.

Commit message format suggestions:
- feat: add <topic/problem> in <language>
- fix: correct <bug> in <file>
- docs: update explanation for <problem>
- style: format <file>

Code Style & Testing
--------------------
- Python: follow PEP8. Use type hints where helpful. Use Black for formatting.
- C++: prefer modern standards (C++17/C++20). Keep functions small and documented.
- Java: adhere to common Java conventions, Javadoc for public methods.
- Provide small example input/output or unit tests if feasible.

Pull Request Checklist
----------------------
- [ ] I have read the [CONTRIBUTING](CONTRIBUTING.md) guidelines (if present).
- [ ] My code compiles / runs and any tests pass.
- [ ] The solution includes a short explanation and complexity analysis.
- [ ] There are no trailing debug prints or unrelated changes.
- [ ] The PR title and description clearly explain the change.

License
-------
This repository can be licensed under a permissive license such as MIT to encourage reuse. Add a LICENSE file in the repo root. Example:
```
MIT License
Copyright (c) 2026 mdzaheerjk
...
```

Contact
-------
Maintainer: mdzaheerjk — https://github.com/mdzaheerjk

Acknowledgements
----------------
- Inspired by GeeksforGeeks, online problem sets, and open-source algorithm collections.
- Contributors and community members who improve explanations and implementations.

Next steps I can take
---------------------
I added language/tool logos and polished visuals in this README. If you want, I can:
- Add a LICENSE, CONTRIBUTING.md, and CODE_OF_CONDUCT.md.
- Create GitHub Actions workflows to run tests and format checks.
- Generate an index (table of contents) linking to each problem folder automatically.

Which of those would you like me to add next?
