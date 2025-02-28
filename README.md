# 🚀 Git Assignment: HeroVired

## 📌 Overview
This repository contains multiple Git-based assignments aimed at strengthening Git workflows, branching strategies, and handling large files using Git LFS. The assignments cover implementing new features in a Python application, managing Git branches efficiently, and working with Git LFS.

---

## 🧮 **Q.1: Implementing Square Root Feature in CalculatorPlus**

### **📂 Project Name:** `git_assignment_HeroVired_1`

### **🛠️ Steps to Complete the Task:**

1. **📁 Create a Repository**  
   - Repository Name: `git_assignment_HeroVired_1`
   - Initialize with a `main` branch.

2. **🌿 Create a `dev` branch and add the following code:**

   ```python
   import math
   
   class Calculator:
       def add(self, a, b):
           return a + b

       def subtract(self, a, b):
           return a - b

       def multiply(self, a, b):
           return a * b

       def divide(self, a, b):
           return a / b

       # 🚀 TODO: Implement the square root function
       def square_root(self, x):
           return math.sqrt(x)
   
   if __name__ == "__main__":
       calculator = Calculator()
   
       num1 = 16
       num2 = 4
   
       print(f"{num1} + {num2} = {calculator.add(num1, num2)}")
       print(f"{num1} - {num2} = {calculator.subtract(num1, num2)}")
       print(f"{num1} * {num2} = {calculator.multiply(num1, num2)}")
       print(f"{num1} / {num2} = {calculator.divide(num1, num2)}")
   
       # ✅ Testing the square root feature
       num3 = 25
       print(f"The square root of {num3} = {calculator.square_root(num3)}")
   ```
![image](https://github.com/user-attachments/assets/b9d4aa5b-d4fa-441e-9cd0-02237c5753f3)
   - git push origin dev
![image](https://github.com/user-attachments/assets/4724747e-5588-4e36-9218-41c00de17b5d)

3. **🔄 Merge `dev` into `main` and release `Version 1` of CalculatorPlus**
![image](https://github.com/user-attachments/assets/455a5920-3df5-4dcb-a298-49a09e6cc3f8)
![image](https://github.com/user-attachments/assets/a7f2a7cd-3987-475c-b73f-6e5cd39ef94f)

5. **👥 Add a classmate as a collaborator**
6. **🌱 Create a `feature/sqrt` branch from `main`**
7. **🐞 Fix a critical bug in `divide` function:**
   ```python
   def divide(self, a, b):
       if b == 0:
           raise ValueError("Cannot divide by zero.")
       return a / b
   ```
8. **🔀 Merge bug fixes into `feature/sqrt` and keep it updated**
9. **🔎 Request a code review from `feature/sqrt` into `dev` branch**
10. **✅ After approval, merge `feature/sqrt` into `dev` and test**
11. **📌 Commit with message `dev test has been done`, push to `dev`**
12. **🚀 Merge `dev` into `main` and release `Version 2`**

---

## 📂 **Q.2: Integrating Git LFS for Large Binary Files**

### **📌 Project Name:** `git_assignment_HeroVired`

### **🛠️ Steps to Use Git LFS:**

1. **🛠️ Install Git LFS:**
   ```sh
   git lfs install
   ```
2. **🌱 Create a new branch `lfs`**
   ```sh
   git checkout -b lfs
   ```
3. **📂 Track large binary files:**
   ```sh
   git lfs track "*.mp4"
   ```
4. **⬆️ Upload a large file (over 200MB) and push:**
   ```sh
   git add .
   git add big_file.mp4
   git commit -m "Added large file to Git LFS"
   git push origin lfs
   ```
5. **📥 Clone repository on another machine and verify files:**
   ```sh
   git clone <repo_url>
   git lfs pull
   ```

---

## 📐 **Q.3: Implementing a Geometry Calculator with Git Stash**

### **📌 Project Name:** `git_assignment_HeroVired`

### **🛠️ Steps to Complete the Task:**

1. **🌱 Create a New Branch for Circle Area Feature:**
   ```sh
   git checkout -b feature/circle-area
   ```
2. **📌 Stash the Changes for Circle Area:**
   ```sh
   git stash
   ```
3. **🌿 Create a New Branch for Rectangle Area Feature:**
   ```sh
   git checkout -b feature/rectangle-area
   ```
4. **📌 Stash the Changes for Rectangle Area:**
   ```sh
   git stash
   ```
5. **🔄 Switch Back to `feature/circle-area` and Retrieve Changes:**
   ```sh
   git checkout feature/circle-area
   git stash pop
   ```
6. **✅ Implement and Complete the Circle Area Feature:**
   ```python
   import math
   
   class GeometryCalculator:
       def calculate_circle_area(self, radius):
           return math.pi * radius ** 2
   ```
7. **📌 Commit and Push Circle Area Feature:**
   ```sh
   git add .
   git commit -m "Implemented circle area feature"
   git push origin feature/circle-area
   ```
8. **🔄 Switch Back to `feature/rectangle-area` and Retrieve Changes:**
   ```sh
   git checkout feature/rectangle-area
   git stash pop
   ```
9. **✅ Implement and Complete the Rectangle Area Feature:**
   ```python
   class GeometryCalculator:
       def calculate_rectangle_area(self, length, width):
           return length * width
   ```
10. **📌 Commit and Push Rectangle Area Feature:**
    ```sh
    git add .
    git commit -m "Implemented rectangle area feature"
    git push origin feature/rectangle-area
    ```
11. **🔄 Create Pull Requests to `dev` Branch:**
12. **🔍 Review and Merge After Approval:**
13. **🚀 Merge Both Features into `main`**

---

## 🎯 **Conclusion**
- ✅ Successfully implemented Git branching strategies.
- ✅ Efficiently managed large files using Git LFS.
- ✅ Used Git stash for handling multiple feature developments.
- ✅ Followed best practices in Git workflows including pull requests and code reviews.

**🎉 Repository is now ready with well-structured feature branches and Git best practices applied! 🚀**


