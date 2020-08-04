from cdqa.utils.converters import pdf_converter
from cdqa.pipeline import QAPipeline
from cdqa.utils.download import download_model
from pathlib import Path

def cdQA(question, firstRun):
    answer = ""
    counter  = 0

    if firstRun:
        #Download pre-trained reader model
        download_model(model='bert-squad_1.1', dir='./models')

    #Convert the PDF files into a DataFrame for cdQA pipeline
    df = pdf_converter(Path(__file__).parent)

    #Instantiate the cdQA pipeline from a pre-trained reader model
    cdqa_pipeline = QAPipeline(reader='./models/bert_qa.joblib', max_df=1.0)
    cdqa_pipeline.fit_retriever(df=df)

    #Execute a query and return the top 3 possible answers
    prediction = cdqa_pipeline.predict(question, 3)

    #Constuct the answer using the top 3 possible answers
    for preditct in prediction:
        counter += 1
        answer += ("Answer #{}: " + preditct[0] + '\n' +
                   "Paragraph: "  + preditct[2] + '\n\n').format(str(counter))

    return answer