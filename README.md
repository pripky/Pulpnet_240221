# Pulpnet_240221
## IITK InfoBot

### Pages Scraped:

Here are the sources used to gather the data from:

#### Institute Counselling Service (ICS)
- [FAQ](https://www.iitk.ac.in/counsel/faq.php)
- [Events](https://www.iitk.ac.in/counsel/events.php)
- [New UG Information](https://www.iitk.ac.in/counsel/new-ug-information.php)
- [New PG Information](https://www.iitk.ac.in/counsel/new-pg-information.php)
- [UG Information](https://www.iitk.ac.in/counsel/ug-information.php)
- [PG Information](https://www.iitk.ac.in/counsel/pg-information.php)

#### Vox Populi – IITK 101 Series
- [Games and Sports Council](https://voxiitk.com/iitk101-games-and-sports-council/)
- [MnC Council](https://voxiitk.com/iitk101-mnc-council/)
- [Science and Technology Council](https://voxiitk.com/iitk101-science-and-technology-council/)
- [Academics](https://voxiitk.com/iitk101-academics/)
- [Academics and Career Council](https://voxiitk.com/iitk101-academics-and-career-council/)
- [Campus Life](https://voxiitk.com/iitk101-campus-life/)
- [Students' Gymkhana](https://voxiitk.com/iitk101-students-gymkhana/)
- [Course Overview](https://voxiitk.com/iitk101-course-overview/)

#### IIT Kanpur Official Academic Page
- [Academics Overview](https://www.iitk.ac.in/futurestudents/acads/)

### Methods employed:

- **Web Scraping**: `requests`, `BeautifulSoup`
- **Text Embedding**: `sentence-transformers` (`all-MiniLM-L6-v2`)
- **Similarity Matching**: Cosine similarity with top-k filtering
- **Question Answering**:
  - `deepset/roberta-base-squad2` (extractive answers)
  - `google/flan-t5-base` (answer elaboration)
- **Frontend Interface**: `Streamlit`

### Instructions on how to run the chatbot:

1. **Clone this repository**  
   ```bash
   git clone https://github.com/pripky/Pulpnet_240221.git
   cd Pulpnet_240221
   ```
2. Create a virtual environment (recommended)
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   source venv/bin/activate  # On Mac/Linux
   ```
3. Install the required packages
   ```bash
   pip install -r requirements.txt
   ```
4. Run with streamlit
   ```bash
   streamlit run app.py
   ```
If you're running the chatbot for the first time, some models will be downloaded automatically. Depending on your internet speed, this may take a few minutes. Please wait patiently while the models load.
