"""
import logging

logging.debug("Debug Message")
logging.info("Info Message")
logging.warning("Warning Message")
logging.error("Error Message")





import logging

logging.basicConfig(level=logging.INFO)

logging.debug("Debug")
logging.info("Information")
logging.warning("Warning")





import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s"
)

logging.info("Program Started")
logging.error("File Missing")





import logging

logging.basicConfig(level=logging.INFO)

name = "Amulya"
score = 95

logging.info(f"{name} scored {score}")
logging.warning("Low Attendance")





import logging

logging.basicConfig(level=logging.ERROR)

logging.info("Connected")
logging.warning("Retrying")
logging.error("Connection Lost")
logging.critical("System Shutdown")






import logging

logging.basicConfig(level=logging.INFO)

try:
    x = 10 / 0
except Exception as e:
    logging.error(e)

logging.info("Program Ended")





import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(message)s"
)

def calculate(a, b):
    logging.info("Calculation Started")
    print(a + b)
    logging.info("Calculation Completed")

calculate(5, 8)






import logging

logging.basicConfig(level=logging.WARNING)

logging.debug("A")
logging.info("B")
logging.warning("C")
logging.error("D")
logging.critical("E")

print("Done")
"""