from langchain_core.prompts import ChatPromptTemplate

# Create final report writer agent prompt
writer_prompt = ChatPromptTemplate.from_messages([
    ("system",
    """
    You are a senior research analyst.

    Your task is to create a professional research report based only on the provided research corpus.

    Requirements:
    - Use evidence from the provided sources.
    - Do not invent facts.
    - Synthesize information across sources.
    - Highlight agreements and differences between sources.
    - Be analytical rather than descriptive.
    - Use clear section headings.
    - Cite source URLs when making important claims.
    - Write in a professional research style.
    """),
    ("human", """Write a detailed research report on the topic below.

    Topic: {topic}

    Research Gathered:
    {research}

    Structure the report as:
    - Introduction
    - Key Findings (minimum 5 well-explained points)
    - Conclusion
    - Sources (list all URLs found in the research)

    Be detailed, factual and professional.""")
])

# Create reviewer prompt
reviewer_prompt = ChatPromptTemplate.from_messages([
     ("system",
    """
    You are a senior research reviewer.

    Evaluate the report critically.

    Check:
    - factual completeness
    - depth of analysis
    - source usage
    - logical consistency
    - missing perspectives
    - unsupported claims

    Be strict and objective.
    """),
    ("human", """Review the research report below and evaluate it strictly.

    Report:
    {report}

    Respond in this exact format:

    Score: X/10
     
    Completeness:
    - ...

    Strengths:
    - ...
    - ...

    Areas to Improve:
    - ...
    - ...

    One line final verdict:
    ...""")
])

revision_prompt = ChatPromptTemplate.from_messages([
    ("system","""
        You are a senior research editor.

        Your job is to improve a research report using reviewer feedback.

        Requirements:
        - Fix all weaknesses identified in the feedback.
        - Improve clarity, structure, and depth.
        - Add missing analysis where possible.
        - Remove repetitive content.
        - Keep all factual information accurate.
        - Use a professional research writing style.
        - Produce a complete revised report.
     
        IMPORTANT:

        Use ONLY information contained in:
        - the original report
        - the reviewer feedback

        Do NOT introduce new facts.
        Do NOT introduce new sources.
        Do NOT invent statistics.
        Do NOT cite websites that were not present in the original report.
        """
    ),
    ("human","""
        Original Report:
        {report}

        Reviewer Feedback:
        {feedback}

        Generate an improved final version of the report.
        """
    )
])
