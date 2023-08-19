

# Django Tailwind CSS Integration Guide

If you're looking to seamlessly integrate Tailwind CSS into your Django project without relying on third-party packages, you're in the right place. This guide will walk you through the process of using Tailwind CSS templates effectively, allowing you to achieve stunning designs without the need for expensive templates. What's more, this design pattern harmoniously accommodates the integration of other CSS frameworks, ensuring a conflict-free styling environment. As an added bonus, this project comes equipped with Flowbite plugins. Plus, you have the flexibility to incorporate additional plugins, thereby supercharging your UI designs.
### Prerequisites.

Before diving into this integration, ensure you have the following prerequisites:

1. Proficiency in Django and Node.js.
2. An integrated development environment (IDE) such as PyCharm, Visual Studio Code, or any editor of your preference.

### Getting Started

Follow these steps to set up the Django project with Tailwind CSS integration. The process is similar across different operating systems, but here we'll outline the steps for WINDOWS.

1. <b>Clone the Repository </b>

Open your terminal and execute the following commands:

```bash
git clone https://github.com/mwangihub/django-tailwind.git
cd django-tailwind
```

2. <b>Run Node.js Environment</b>

In the same terminal window, execute the following:

```bash
npm install # Install required Node.js packages
npm run dev # Compile Tailwind CSS

```
3. <b>Set Up Python Virtual Environment</b>
Open a new terminal window and navigate to the project directory:

```bash 
cd django-tailwind
```

Create and activate a Python virtual environment:

```python
python -m venv venv      # Create the virtual environment
.\venv\Scripts\activate  # Activate the virtual environment
```

3. <b>Install Django Dependencies</b>


While the virtual environment is active, install the required Python packages:
```python 
pip install -r requirements.txt
```
3. <b>Run the Django Development Server</b>

Finally, start the Django development server:

```bash
python manage.py runserver
```
- Now you can access your Django project with Tailwind CSS integration by visiting http://127.0.0.1:8000 in your web browser.

By following these steps, you've successfully integrated Tailwind CSS into your Django project without relying on third-party packages. This method allows you to harness the power of Tailwind's styling capabilities while maintaining the flexibility to incorporate other CSS frameworks seamlessly. Feel free to explore and enhance your UI designs by incorporating additional plugins or customizations.