import click
import csv_reader
from rag_retriever import RAGRetriever
from concept_extractor import rule_based
from transformers import pipeline

@click.command()
@click.option('--subject', required=True, help='Name of subject CSV file (without .csv)')
def main(subject):
    path = f'{subject}.csv'
    rows = csv_reader.read_csv(path)
    questions = [r['Question'] for r in rows]

    # Build RAG retriever on questions themselves (for demo)
    retriever = RAGRetriever(questions)

    # Load free LLM (e.g., distilbert summarization -> repurpose for concept tagging)
    llm = pipeline('text2text-generation', model='google/flan-t5-small')

    out = []
    for row in rows:
        qnum = row['Question Number']
        q = row['Question']
        # RAG: retrieve similar questions
        contexts = retriever.retrieve(q)
        prompt = f"Identify the historical concepts tested in the following question:\nQuestion: \"{q}\"\nRelevant context: {contexts[:2]}\nConcepts:"
        resp = llm(prompt, max_length=64)[0]['generated_text']
        llm_concepts = [c.strip() for c in resp.split(',') if c.strip()]
        rule_concepts = rule_based(q)
        concepts = sorted(set(llm_concepts + rule_concepts))
        out.append((qnum, q, concepts))

    # write out
    with open('output_concepts.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Question Number', 'Question', 'Concepts'])
        for qnum, q, concepts in out:
            writer.writerow([qnum, q, '; '.join(concepts)])
            print(f"Question {qnum}: {', '.join(concepts)}")


if __name__ == '__main__':
    main()
