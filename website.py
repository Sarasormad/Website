from flask import Flask, render_template, send_from_directory

app = Flask(__name__)


@app.route("/")
def home():
    profile = {
        "name": "Sara Madjdi-Sorkhabi",
        "title": "Computer Science & Statistics Student | Aspiring Quant Researcher",
        "bio": (
            "I am a senior at California State University, Northridge (B.S. in "
            "Computer Science and Statistics, expected May 2026) focused on quant "
            "research, data science, and data analytics. I enjoy building reproducible "
            "data pipelines, developing statistical and machine learning models, and "
            "turning large datasets into practical decisions."
        ),
        "image": "images/headshot.png",
    }

    experience = [
        {"name": "JPL Data Analyst Intern", "link": "/experience/jpl-intern"},
        {"name": "NSF Assistant Researcher", "link": None},
    ]

    projects = [
        {
            "title": "JPL Flight Data Benchmarking",
            "description": (
                "Analyzed 350K+ proprietary entries to improve training efficiency "
                "and benchmarking quality for JPL flight-related projects."
            ),
            "details": (
                "Engineered features by combining internal and external sources, "
                "built reproducible visual analysis in Power BI/Seaborn, and "
                "presented actionable recommendations to division leadership."
            ),
            "learn_more": "/experience/jpl-intern",
        },
        {
            "title": "ASL Sign Language Interpreter",
            "description": (
                "Building a real-time computer vision system with Python, OpenCV, "
                "and PyTorch to classify ASL gestures and convert prediction translations from "
                "text to speech output."
            ),
            "details": (
                "Built a custom ASL Sign Language Dataset using OpenCV and MediaPipe, "
                "developed a real-time gesture pipeline, trained classifiers on labeled "
                "hand-sign data, and evaluated performance with iterative preprocessing "
                "and augmentation to improve robustness."
            ),
        },
        {
            "title": "AI Mentorship Platform for Intro to Mechanical Engineering",
            "description": (
                "Led a 10-student team to build a mentorship platform with Flask, "
                "React, and SQL for personalized support in Intro to Mechanical "
                "Engineering."
            ),
            "details": (
                "Built a course-restricted assistant for ME101 using a RAG pipeline so "
                "students can ask ChatGPT-style questions answered only from approved "
                "CSUN course materials. Added a quiz-generation tab that creates "
                "multiple-choice practice questions by topic from the same uploaded "
                "materials, and developed a personalized analytics dashboard that tracks "
                "quiz performance metrics to help students identify weak areas."
            ),
        },
        {
            "title": "Multi-Criteria Shortest Path Optimization",
            "description": (
                "Extended Dijkstra's algorithm with dual edge weights in Java/Python "
                "to evaluate trade-offs in multi-objective routing."
            ),
            "details": (
                "Compared runtime and quality trade-offs against standard shortest-path "
                "methods and documented how multi-objective constraints affect route "
                "selection and complexity."
            ),
        },
        {
            "title": "Early Detection of Cocoa Seed Infection",
            "description": (
                "Developing computer vision models in Python and PyTorch to detect "
                "early-stage cocoa seed infection with EfficientNet architectures."
            ),
            "details": (
                "Applied image preprocessing and augmentation workflows to improve "
                "model performance and evaluated architecture-level trade-offs for "
                "early detection accuracy."
            ),
        },
        {
            "title": "NSF Higher Criticism Research",
            "description": (
                "Implemented statistical computing methods in R for large-scale "
                "multiple testing and high-dimensional inference."
            ),
            "details": (
                "Built bootstrap resampling workflows from scratch to support "
                "Higher Criticism research and contributed to computationally "
                "efficient methods for modern statistical inference."
            ),
        },
    ]

    gallery_images = [
        {"src": "images/IMG_B627A70E6443-1.jpeg", "alt": "Gallery photo one"},
        {"src": "images/IMG_8704.JPG", "alt": "Gallery photo two"},
        {"src": "images/IMG_8519.jpg", "alt": "Gallery photo three"},
    ]

    recognitions = [
        "Outstanding Undergraduate Mathematics Award",
        "Leslie and Terry Cutler Scholarship Endowment in Science and Mathematics",
        "NASA Open Science Certification",
        "Magna Cum Laude standing (GPA: 3.8/4.0)",
    ]

    contact = {
        "email": "sarasormad@gmail.com",
        "linkedin": "https://www.linkedin.com/in/sarasormad",
        "github": "https://github.com/sarasormad",
        "resume": "/resume",
    }

    return render_template(
        "index.html",
        profile=profile,
        experience=experience,
        projects=projects,
        gallery_images=gallery_images,
        recognitions=recognitions,
        contact=contact,
    )


@app.route("/experience/jpl-intern")
def jpl_intern():
    details = {
        "title": "JPL Data Analyst Intern",
        "team": "NASA Jet Propulsion Laboratory",
        "description": (
            "During my JPL Data Analyst Internship, I analyzed proprietary "
            "flight-support datasets (350K+ records) to improve training efficiency "
            "and benchmarking quality for mission-related workflows, including Mars "
            "2020 support activities. I built reproducible data processing and "
            "feature-engineering pipelines in Python, developed visual analytics "
            "in Power BI and Seaborn, and translated findings into recommendations "
            "for technical and leadership stakeholders. My work focused on reliable "
            "evaluation, traceable experimentation, and practical decision support "
            "in a high-stakes research environment."
        ),
        "papers": [
            {"title": "JPL Internship Final Report", "url": "/files/JPLreport.pdf"},
        ],
    }
    return render_template("jpl_intern.html", details=details)


@app.route("/files/<path:filename>")
def serve_file(filename):
    return send_from_directory(".", filename)


@app.route("/resume")
def serve_resume():
    return send_from_directory(".", "sara_resume_spring26.pdf")


if __name__ == "__main__":
    app.run(debug=True)
