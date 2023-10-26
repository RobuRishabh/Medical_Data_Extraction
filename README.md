# Medical_Data_Extraction

Before starting the project you need to add install all the libraries in requirement.txt file.

Also you need to install some dependencies

1. poppler-windows : You can download it from here "https://github.com/oschwartz10612/poppler-windows/releases/"just click on the release a folder will get downloaded. Extract that folder into your C-drtive
2. Google Tesseract engine : You can download it from here "https://github.com/UB-Mannheim/tesseract/wiki"

## Project Overview
Whenever we go to any hospital, we have to fill a lot of documents, and hospitals do these so that they can submit the claims to the insurance companies.

These documents can be patient Medical Record or prescription. So, these hospital just scan the documents and send it to the insurance companies were the companies have to extract the meaningful data from these documents.

To make this work easier for the companies we follow these steps :
1. PDF to Image Conversion:
- Convert the PDF documents into images using the "pdf2image" module.
Image Pre-processing:

2. Enhance the quality of the images to improve extraction accuracy.
- Utilize image processing techniques, such as adaptive thresholding, in place of simple thresholding.
- Adaptive thresholding adjusts the threshold dynamically based on regions of the image.

3. Text Extraction with OpenCV:
- Apply OpenCV, a computer vision library, to process the images.
- Perform text extraction from the processed images using the pytesseract OCR engine, which is based on Google's Tesseract.

4. Data Extraction:
- Use regular expressions (regex) to extract specific information from the extracted text.
- Identify and extract relevant details such as names, dates of birth (DOB), medicine names, billing information, addresses, and other required data.

5. Frontend and Verification:
- Develop the project's backend to manage data extraction and processing.
- To verify the project's results and facilitate interaction with the backend, create a frontend interface.
- Consider using FASTAPI for building the frontend.

6. Optional: AWS Textract Integration:
- While AWS Textract is a paid service, it can be an alternative for text extraction if budget allows.
- Integrate AWS Textract into the project to extract text from images using Amazon's OCR service.