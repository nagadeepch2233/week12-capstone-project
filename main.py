import asyncio
from src.services.portfolio_service import PortfolioService
from src.utils.decorators import section
from src.utils.formatter import formatted_output
from src.utils.logger import log
from src.utils.async_helpers import delay_print

class PortfolioApp:

    def __init__(self):
        self.service = PortfolioService()

    @section("SKILLS DEMONSTRATED:")
    def skills(self):
        skills_list = [
            "Advanced Python: Generators, decorators, context managers",
            "Web Development: Full-stack with frameworks",
            "Database Design: Complex relationships, optimization",
            "DevOps: Docker, Kubernetes, CI/CD, cloud deployment",
            "Testing: Unit, integration, E2E, performance testing",
            "Security: Authentication, authorization, data protection",
            "System Design: Scalable architecture, microservices patterns"
        ]
        for skill in skills_list:
            print("✅", skill)
            self.service.add_entry("SKILL", skill)

    @section("LEARNING JOURNEY DOCUMENTATION:")
    async def learning_journey(self):
        journey = [
            "Week 1-4: Python fundamentals, built Personal Finance Tracker",
            "Week 5-6: OOP and APIs, built Weather Dashboard",
            "Week 7-8: Flask web apps, built blog platform",
            "Week 9: REST APIs, built Task API",
            "Week 10: Advanced Python concepts",
            "Week 11: DevOps and deployment",
            "Week 12: Capstone project"
        ]
        for step in journey:
            await delay_print(step)
            self.service.add_entry("JOURNEY", step)

    @section("CAREER PREPARATION:")
    def career(self):
        points = [
            "Portfolio: 6 complete projects",
            "GitHub: Clean repos, documentation",
            "Resume: Quantifiable achievements",
            "Interview ready",
            "Networking with Python community"
        ]
        for p in points:
            print("👉", p)
            self.service.add_entry("CAREER", p)

    async def run(self):
        log("Starting Portfolio Application...")

        with formatted_output():
            self.skills()
            await self.learning_journey()
            self.career()

        self.service.export_to_file()
        log("Application finished successfully!")

if __name__ == "__main__":
    app = PortfolioApp()
    asyncio.run(app.run())
