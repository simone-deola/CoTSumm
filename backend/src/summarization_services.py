from backend.src.connector.ChatGPT_connector import ChatGPTConnector


class SummarizationService:
    def __init__(self):
        self.connector = ChatGPTConnector()


    def summarize(self, text):

        report=[]

        ### GET FIRST SUMMARY
        print("GET FIRST SUMMARY")
        _prompt = f"Given the text: '{text}' \n Summarize it in 100 words"
        initial_summary = self.connector.prompt(_prompt) ### COST REDUCTION

        report.append(_prompt)
        report.append(initial_summary)

        ### GET MAIN TOPICS
        print("GET MAIN TOPICS")
        _prompt = f"Given the text: '{initial_summary}' \n Extract two notions not explained in this text. List them in a coma separated list, with no additional text."
        topics = self.connector.prompt(_prompt) ###COST REDUCTION
        report.append(_prompt)
        report.append(topics)


        topics = topics.split(",")
        ### EXPAND TOPICS
        print("EXPAND TOPICS")
        _expanded_summary = initial_summary
        for t in topics:
            _prompt = f"Given this summary: '{_expanded_summary}' \n Repeat the previous text and add inside the same text a short definition of the notion '{t}'. Keep the rest of the text unchanged."
            _expanded_summary = self.connector.prompt(_prompt)
            report.append(_prompt)
            report.append(_expanded_summary)

        print("END")
        return _expanded_summary, report