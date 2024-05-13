# Responsible AI in Academia

**Author:** _Kieran Lindsay_ (ORCID: 0000-0002-1624-7679) | **First published:**
March 31, 2024 | **Last update:** May 13, 2024 _(see file history for
versions)_

_This is a living document. It is open source, and anyone is welcome to make
suggestions. You can find the source and document history
[here](https://github.com/Academic-ID/academicAI) or reach out to Kieran at
kieran@academicid.net_

---

It is an exciting time for AI research and the use of AI in research. Generative AI has the potential to accelerate and enrich
many aspects of the research process, from hypothesis generation to data
analysis to dissemination. However, to ensure the reproducibility and integrity
of research that involves or utilises generative AI, it is vital to be
transparent about its use.

We are still learning about this technology's impact and are faced with an ever-growing array of AI models, all with different strengths and a wide array of usage parameters. As such, it is essential that generative AI users are transparent and specific in reporting on its use. Providing specific details on AI use will help the community build a clearer picture of AI capabilities and move the field forward.

Below are some preliminary guidance principles that academics, researchers and students
can follow when using generative AI to assist with their research or in situations where generative AI forms the subject of their research.

These guidelines are preliminary and are being incrementally expanded and
improved. They are designed as a starting point from which the risks, mitigations, and reporting on specific AI use cases can be developed. As such, these should not be relied on solely but used in conjunction with established research procedures, best practices, methodologies and ethics guidelines.

## How Generative AI Works: A Primer

Generative AI is a subset of artificial intelligence that focuses on creating new content, such as text, images, audio, or video, based on learned patterns from existing data. The most common type of generative AI is the language model, which can produce human-like text after being trained on vast amounts of written material.

### Training Process

There are many variations used for training generative AI models. Typically, training involves feeding the model a large dataset, such as a corpus of books, articles, or websites. The AI system analyses this data to identify patterns and relationships between words, phrases, and concepts. For example, a language model might learn that the word "king" is often associated with words like "queen," "castle," and "throne," and that it frequently appears in sentences about royalty, power, and medieval times.

This first stage of the learning process is based on a technique called "unsupervised learning," where the AI is not given explicit labels or categories for the data, but rather discovers patterns on its own. The model adjusts its internal parameters to capture these patterns better, essentially building a statistical representation of the language.

Most models then undergo some form of supervised fine-tuning on a smaller dataset for a specific task, such as question answering, text summarisation, or sentiment analysis. This involves providing the model with labelled examples of the desired behaviour and updating its parameters to minimise the difference between its predictions and the correct labels.

Some models incorporate human feedback into the training process to better align the model's outputs with human preferences and values. This can involve having humans rate the quality or appropriateness of the model's outputs and using this feedback as a reward signal to update the model's parameters via reinforcement learning. For example, if the model generates a text that humans deem offensive or biased, it would receive a negative reward, encouraging it to avoid such outputs in the future.

The training process is often iterative, with model creators fine-tuning and adjusting the model based on its performance and user feedback. This can involve updating the training data, modifying the model architecture, or tweaking hyperparameters to improve the model's outputs.

It is important to note that the specific training process varies widely depending on the type of generative AI model, the intended application, and the researchers' goals and resources. Some models may rely primarily on unsupervised pre-training, while others may place greater emphasis on human feedback and alignment. Some models replace the human feedback step with feedback from more powerful models such as GPT-4.

Training is the most significant part of a model's development in influencing performance and behaviour. The key takeaway here is that different models will have vastly different capabilities and behaviours and, for lack of a better phrase, statistically influenced worldviews. Model creators train their models to meet the specifications the creators desire, and, as a result, when assessing a generative AI model for use, it is vital to consider the goals and values of the model's creator.

### Neural Networks and Transformers

Most modern generative AI systems are based on artificial neural networks designed to loosely mimic the human brain's structure. These networks consist of interconnected nodes (or "neurons") organised into layers. Each node performs a simple computation based on the inputs it receives from nodes in the previous layer and passes the result to nodes in the next layer. Through this process, the network can learn to recognise complex patterns and relationships in the data.

A particularly influential neural network architecture for generative AI is the "transformer," introduced in a [2017 paper](https://proceedings.neurips.cc/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf) by Ashish Vaswani et al. The transformer uses a mechanism called "attention" to weigh the relevance of each part of the input data to the current prediction task.

This attention mechanism allows the model to capture long-range dependencies in the data more effectively than previous architectures. It has been the basis for many state-of-the-art language models, such as GPT (Generative Pre-trained Transformer) and BERT (Bidirectional Encoder Representations from Transformers).

### Generating New Content

Once a generative AI model has been trained, it can be used to generate new content by providing it with a prompt or seed input. For a language model, this might be the beginning of a sentence or paragraph, which the model then tries to complete based on the patterns it has learned.

The generation process is probabilistic - at each step, the model predicts a distribution over possible following words or tokens and then samples from that distribution to choose the next word or token to generate. This sampling process can be adjusted to make the model's output more or less "creative" or unpredictable.

For example, suppose we prompt a language model with the phrase "The old king lived in a...". The model might predict a high probability for words like "castle," or "palace," based on the patterns it has seen in its training data. It would then likely generate one of these words to complete the sentence. However, if we adjust the sampling parameters to be more adventurous, it might generate a less expected word like "spaceship" or "treehouse," leading to a more surprising or imaginative output.

Usually, the user can control some of these parameters and adjust them to fine-tune the model's outputs for a specific task or application. For example, in a creative writing context, a higher sampling temperature might be used to encourage more diverse and unexpected outputs. In contrast, a lower temperature might be preferred in a summarisation task to ensure the model sticks closely to the input data and, thus, outputs more deterministic content. This is important as the parameters set by the user can influence the model's outputs, and as such, the user must be aware of these parameters and their impact on the model's outputs.

When discussing the size or complexity of a generative AI model, it is common to refer to the number of tokens it can process or generate. [A token is a basic unit of text that is used as an input or output for a model](https://platform.openai.com/tokenizer). Tokens can be individual words, subwords (parts of words), or even single characters, depending on the specific tokenisation method used.

For example, consider the sentence: "The quick brown fox jumps over the lazy dog." A word-level tokeniser would split this into the following tokens: ["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]. However, a subword tokeniser might break down less common words into smaller parts, like this: ["The", "quick", "brown", "fox", "jump", "##s", "over", "the", "lazy", "dog"], where "##s" is a special token indicating that it should be attached to the previous token.

End users have little control over the tokenisation process; however, when assessing the capabilities of a model, the number of tokens a model can process or generate is a necessary metric to consider. For example, it will be necessary to utilise a model with a larger token window if the user is processing long documents. Most models will provide a rough token-to-word conversion estimate. For example, [OpenAI provides a general rule of thumb](https://platform.openai.com/tokenizer): one token equals roughly four characters, or 100 tokens equate to roughly 75 words.

## Risks of Generative AI

Addressing the risks associated with generative AI use requires awareness.
Fostering a culture of critical engagement with generative AI is the best method
to help mitigate the risks.

The use of generative AI – either as part of day-to-day activities, or within a
specific research methodology, or as the object of research – introduces a range
of risks that require consideration. A selection of the most obvious risks are
highlighted below. Users of generative AI should undertake further research into
the risks for specific use cases, especially when using generative AI as part of
a research methodology.

### Ethical Risks

1. **Bias and Fairness:** Generative AI systems, reflecting biases in their training data, can perpetuate or exacerbate biases. This risk is particularly concerning in applications that may impact decision-making in critical areas such as healthcare, justice, and employment or the use of generative AI in qualitative or research methodologies involving any degree of subjective assessment. For instance, a generative AI model trained on historical medical data might inherit biases against certain demographic groups, leading to skewed research outcomes reinforcing health disparities.

2. **Alignment and Control:** As noted above, it is vital to remember that companies train large language models for performance, safety and alignment, not necessarily balance and that it is up to these companies to determine what alignment is. Alignment is usually a metric that considers how the model's behaviour matches what the intended human user expects. For general-purpose or consumer-focused large language models, this alignment is usually to the average user (or whatever the most number of paying customers may prefer in a language model). However, the influence of the creator's personal views in training the models cannot be [discounted](http://dx.doi.org/10.1111/ajps.12408). As such, it is essential to consider the alignment of the model in the context of the intended user's and model creator's goals and values. This approach to alignment and safety can lead to the model refusing to respond on a topic, producing outputs that are not in line with the research's objectives or outputs biased towards a particular ideological or [political view](http://dx.doi.org/10.1007/s11127-023-01097-2). Moreover, the alignment of generative AI models can change over time as companies update their training data, algorithms, or content policies. This can create challenges for longitudinal research projects that rely on consistent and predictable model behaviour.

3. **Privacy Concerns:** The use of generative AI in processing and synthesising
   data can inadvertently lead to privacy breaches, especially when dealing with
   sensitive or personal information. The ability of these systems to generate
   detailed synthetic data based on real-world datasets poses a risk of
   re-identification of individuals whose data has inadvertently entered the
   training set. Further, even when using models where data is not used for retraining, sending data to third-party companies may breach contractual or legislative privacy provisions.

4. **Intellectual Property and Plagiarism:** Generative AI's capacity to produce
   content that closely mimics existing copyrighted material raises concerns
   about unintentional plagiarism and the violation of intellectual property
   rights. While this remains a legal grey area, the concern remains particularly problematic in academic settings where the originality of research outputs and the proper attribution of knowledge are paramount.

### Operational Risks

1. **Reliability and Reproducibility:** The stochastic nature of generative AI
   models means that they can produce inconsistent results, challenging the
   reproducibility of research findings. This variability, coupled with the
   'black box' nature of many AI systems, can make it difficult to understand
   and explain how specific results were generated, undermining research's
   reproducibility, credibility and integrity. For instance, two researchers using the same generative model but with slightly different parameters will likely get divergent results, making it impossible to replicate findings.

2. **Overreliance and Skill Degradation:** The convenience and efficiency of
   generative AI tools can lead to an overreliance on automated systems,
   potentially atrophying critical research skills such as literature review,
   data analysis, and even the formulation of research questions. This
   overreliance could also lead to researchers accepting AI-generated insights
   without sufficient scrutiny, increasing the risk of propagating errors or
   flawed analyses.

3. **Writing Style and Quality** This risk of overreliance extends to the use of generative AI for writing published academic material. Whilst anecdotal, most proficient in English will readily question text that uses overly verbose, archaic or unneedingly positive language. In addition to the positive style that models are trained to mimic, most generative AI systems have some form of frequency/presence penalty parameter that discourages the repeated use of the same tokens within close proximity. While this helps prevent the model from getting stuck in loops outputting repeated phrases and words, it can result in an expanded vocabulary that is not always warranted. While the impact on style, readability and substance is obvious, these may be forgiven, to an extent, for the time-saving benefit. However, when content is purported to be human-written, drops in quality *[may](https://arxiv.org/pdf/2404.01413)* result in a feedback loop amplifying these deficiencies as models are retrained on this "human-generated" content.

4. **Regulatory and Legal Risks:** The rapid improvement in capabilities of generative AI and its applications significantly outpace existing legal and regulatory frameworks, leading to uncertainties and potential non-compliance. Further, and more generally, while it may be tempting to copy any and all data into ChatGPT to have it summarised, sending this data to a third-party company (potentially out of your jurisdiction) may be a breach of contract or privacy-focused legislation. With the massive amount of computing resources required to power AI models, without specific assurances as to where data is processed by an AI model, it may be sent to multiple jurisdictions that you are unaware of, potentially breaching data sovereignty laws.

## Guidelines for Using Generative AI to Assist Academic Research

Now that we are aware of some of the risks associated with generative AI use, it is
important to consider how we can mitigate these risks. Using generative AI in a
manner consistent with ethical and legal obligations is not complicated;
however, it does require some thought. Below are some guidelines for best
practices that will serve as a starting point for the ethical and responsible
use of AI in academic settings. These guidelines are not exhaustive and should
be applied with a level of discretion aligning with the user's comfort and familiarity with the technology; additional considerations should be incorporated based on the identified risks and the specific use case.

It can be hard to determine the best practices for using generative AI in academic research, as the technology is still evolving. This is more challenging for those without a technical background, as the technology is often opaque and difficult to understand. The best way to overcome this is to use the technology frequently and in lower-stakes situations. The more you use the technology, the greater your intuitive understanding of its strengths and weaknesses will be. This will allow you to understand better the technology and its limitations and, thus, the risks it may present in your research.

It should also be noted up front that general consumer-facing generative AI services, such as the ChatGPT, Gemini or Claude user interfaces, may not be suitable in situations where generative AI forms part of a research methodology and needs to be reproduced. These services are subject to change, and the parameters used to generate responses are not always public. As such, it is recommended that programmatic solutions or customisable playgrounds be used where possible. You can usually find these playgrounds by signing up for developer accounts or searching something along the lines of 'OpenAI API playground'. This will allow for the control and reporting of parameters used in the research, which is essential for any research that others may want to reproduce. However, with the risks noted above in mind, consumer-facing services are likely suitable for exploratory research when testing generative AI or just day-to-day use of the tool.

### Transparency and disclosure

- Always disclose when generative AI has been used to assist with any part of
  the research process, from ideation to data analysis to writing. This should be noted in the methodology section or code made available through a transparent, public repository like GitHub. Where reproducibility of research is essential, it is vital to use and note a specific model version. For example, instead of just using the `gpt-4-turbo` model, which points to whatever the most recent model version is, specify the exact version used, such as `gpt-4-turbo-2024-04-09`. This will allow for the reproduction of the research and ensure that the model used is consistent across all research outputs. Similarly, most models have a wide range of customisable parameters that influence model behaviour, even if these are not altered from the default, they should be clearly noted.

  Being aware of these parameters should be a minimum requirement for
  any use of generative AI as part of a research methodology or when testing
  generative AI as part of your research. As such, using programmatic solutions
  or customisable playgrounds should be preferred over user interfaces such as
  ChatGPT, where these parameters are not always public and are likely to change
  (e.g., in the event of model upgrades or AB testing by OpenAI).

  A full list of accessible model parameters and potentially time-specific information returned from API use by different models can usually be found on their API documents page. For example, OpenAI's API documentation can be found [here](https://platform.openai.com/docs/api-reference/chat/create).

  For example, one may report on the use of generative AI in the following manner:

> We used OpenAI's `GPT-4-Turbo` model to generate potential interview questions that were reviewed and validated by the research team. The specific generative AI parameters used were as follows:

> - model="gpt-4-turbo-2024-04-09"
> - temperature=1,
> - max_tokens=256,
> - top_p=1,
> - frequency_penalty=0,
> - presence_penalty=0,
> - seed=123,
> - system_fingerprint="abc123"
> - ...

- Describe how the AI was used - e.g. brainstorming ideas, literature searches,
  data coding, writing sections of the paper, etc.
- Ensure all prompts used and any system prompts are documented. Prompts are likely to change over time as researchers test and iterate based on the model's output. Where only a final prompt is used for the research goals, only this needs to be documented. However, recording prompt versions is vital in scenarios where the evolution of prompts forms a part of the research (e.g., finding out the ideal prompt to achieve outcome X).
- If knowledge is provided to the large language model (LLM), i.e. in the form
  of uploaded documents or other
  [RAG](https://blogs.nvidia.com/blog/what-is-retrieval-augmented-generation/)
  implementations, make sure this, too, is documented.
  - For example, if using a tool to convert PDF files to text before feeding them to the LLM, you must record the name of the tool, the dates it was used, and any other relevant details. The form of the outputted text and any other relevant observations should be noted. This is important as the quality and form of text provided to LLMs can significantly influence the responses. If the text is in Markdown format, for example, the existence of headings, denoted by hashtags, may be interpreted differently by the LLM compared to if the document was plain text with no headings or formatting present.
  - It may not be feasible or even possible to document all knowledge, especially where you may not be aware of the knowledge provided to the LLM as part of the AI system. It is sufficient to record this as comprehensibly as possible. For this reason, however, it is recommended that AI playgrounds or API endpoints be used where possible, as these will provide a more controllable environment that can be reproduced as needed.

### Human oversight and editorial control

- While AI can assist various stages of research, final decisions, analysis, and
  write-up should be human-led. For example, if an AI is used to generate potential themes from qualitative data, the researchers should manually review, refine, and interpret these themes rather than presenting them directly as findings.
- Carefully fact-check and validate any AI-generated content. Do not assume it
  is accurate.
  - For example, if an AI system is used to draft a literature review, the researchers should verify each cited source and claim made by the AI. AI may speed up the literature review process in this scenario by writing and summarising the content. However, the risks of inaccuracies and hallucination still require some manual effort from the researcher to review and validate.
- Maintain editorial control – a human researcher should always have the final
  say over a paper's content and conclusions. Even if substantial parts of a paper are AI-generated, the human authors should critically review and edit the entire manuscript before submission.
  - The submission of AI-generated content needs to be carefully considered. Not only does the content need to be closely reviewed, but the journal's or conference's publishing guidelines need to be considered. For example, some journals may require a statement on the use of AI in the research, while others may require the AI-generated content to be clearly marked as such. Some publishers will not accept AI-generated content.

### Respect intellectual property

- Be vigilant about AI reproducing copyrighted text or images in its outputs. AI models cannot be relied on to provide references. The scenarios where AI-generated content should be added to a body of text without the author having already found and reviewed relevant sources are limited. Proper attribution should always be given to the original creators of any content used in research. If using generative AI to speed up the writing process or paraphrase text, ensure that the AI-generated content is sufficiently original and distinct and that proper attribution to the ideas in the text is made.
- It should always be remembered that AI systems are trained on existing content. While this does not mean that they cannot produce predicted text that is unique or makes novel connections between ideas, it does mean, at its core - and just like human research, the AI system is using previous knowledge to generate new knowledge. Unfortunately, AI systems do not have an awareness or catalogue of their training data in the sense that if prompted as to the source or inspiration for generated content, the AI system cannot accurately reproduce the piece or pieces of training data it was drawing from. Unless the concept is well known and secondary sources in the training data referring to the origin of the concept exist, AI systems are more likely to hallucinate a source. For example, an AI system will likely know the origin of highly cited experiments due to other training material making the connection between the experiment, the outcomes and the authors; however, for more obscure or recent knowledge, an AI system is more likely to hallucinate a source.

### Consider research ethics

- Using AI does not circumvent standard research ethics protocols. Studies still require ethics approval where applicable, and the incorporation of generative AI may increase the need for ethics oversight. Research ethics committees should be informed about the use of generative AI and its potential implications for the study design, data handling, and participant privacy.
- Researchers should carefully consider the potential ethical risks and challenges posed by generative AI, such as biased outputs, privacy breaches, or unintended consequences, and develop appropriate mitigation strategies. This may involve additional training for research staff, more stringent data protection measures, or regular audits of the AI system's performance.
- When using generative AI to analyse sensitive data, such as personal information, medical records, or social media posts, researchers must ensure that they have obtained the necessary informed consent from participants **and that the use of AI is clearly communicated in the consent process**. Participants should be made aware of how their data will be processed by the AI system, who will have access to the outputs, and any potential risks or benefits.
- Take all practical steps to remove personally identifying information from data before feeding it to an AI system. This may involve techniques such as anonymisation, pseudonymisation, or data masking. However, researchers should be aware that even anonymised data may still be re-identifiable when processed by powerful AI systems, especially if combined with other datasets.
- Consider the potential for generative AI to produce outputs that could be harmful or distressing to research participants, such as generating realistic but fake images or videos of individuals. Researchers should carefully weigh the benefits and risks of using such outputs and implement appropriate safeguards, such as content filtering or human review, to prevent unintended harm.
- Consider potential negative impacts or unintended consequences of the research as a result of AI usage, such as bias or over-reliance by involved researchers. For example, if a generative AI model is used to analyse qualitative data, such as interview transcripts, researchers should be cautious about relying too heavily on AI-generated insights and ensure that they still engage in manual coding and interpretation or review to capture nuances and context that the AI may miss.
- Develop clear guidelines and protocols for the use of generative AI in research projects, including criteria for when it is appropriate to use, how it will be integrated into the study design, and how the outputs will be validated and interpreted. These guidelines should be regularly reviewed and updated as the technology evolves and new ethical considerations emerge.

### Data protection and privacy

- Ensure that any data used in AI models is handled in compliance with data protection regulations and ethical guidelines. This includes regulations such as the General Data Protection Regulation (GDPR) in the European Union, the Privacy Act 1988 and relevant state laws in Australia, the Health Insurance Portability and Accountability Act (HIPAA) in the United States, and other relevant national or regional laws. Researchers should familiarise themselves with the specific requirements of these regulations, such as obtaining informed consent, protecting personal data, and ensuring the right to access and rectify data.
- Where possible, use open-source models or tools that do not require the sharing of sensitive data with third parties. Proprietary AI systems often involve sending data to external servers for processing, which can increase the risk of data breaches or misuse. By using open-source tools that can be run locally or on secure servers, researchers can maintain greater control over their data and reduce the attack surface for potential privacy violations.
- When using cloud-based AI services, choose reputable providers that offer strong data protection guarantees and comply with relevant regulations. Ensure that the cloud servers are located in a jurisdiction with adequate data protection laws and that there are clear contractual agreements in place governing the use and retention of data. Be aware of any cross-border data transfers and ensure that these comply with applicable regulations.

### Reproducibility and data availability

- Aim to use open-source AI models where possible to aid reproducibility. Proprietary models can be significantly more expensive, and the black-box nature of these models means that the parameters used in the research may not be public. This can make reproducing the research difficult.
- Always ensure that the parameters noted in the `Transparency and disclosure` section above are reported.
- Share code, data and methodology to allow other researchers to verify and build upon the work. This can be done by uploading the AI model, code used, parameters, and input data to a repository like GitHub or Huggingface. These platforms provide version control and long-term archiving, making it easier for other researchers to access and use the materials.
- Consider using standardised formats and protocols for sharing AI models and data to promote interoperability and make it easier for other researchers to use and integrate the materials into their own work.
- Provide clear documentation and instructions for using the shared materials, including any dependencies, hardware requirements, or potential limitations.
- Archive versioned copies of AI models or datasets used, as these can change over time. This is particularly important for research relying on rapidly evolving AI technologies, where models and datasets may be updated or replaced frequently.

### Mitigate bias

- Be aware that AI models can reflect [biases present in their training data](https://dl.acm.org/doi/10.1145/3597307),
  which may lead to biased outputs.
- Actively seek out and use diverse datasets for training and testing AI models to ensure they are exposed to a wide range of perspectives, experiences, and demographics.
- Engage with stakeholders and domain experts from different backgrounds to gain insights into potential sources of bias and validate AI model outputs' fairness.
- Take steps to identify and mitigate potential biases, such as testing the model on diverse datasets and examining outputs for stereotyping or unequal treatment. Run controlled tests before utilising a specific model to see if an AI model generates different results for different demographic groups.
- When possible, develop and apply quantitative metrics for measuring bias in AI models, such as demographic parity, equalised odds, or disparate impact.
- Always document and report any identified biases or limitations in the AI model and the steps taken to address them.
- Consider the societal impact and potential for discrimination arising from the
  use of an AI model. For example, if researching an AI system for its ability to make decisions that affect people's lives (e.g. in medical diagnosis or hiring), extra care must be taken to ensure fairness and non-discrimination.

### Maintain academic standards

- The use of AI should not compromise the research's quality, rigour, or
  integrity.
- Ensure that the use of AI aligns with the study's research questions, hypotheses, and objectives. A clear rationale should drive the incorporation of AI and should not be used simply because it is available or trendy.
- Contextualise the use of AI within the broader landscape of the research field, acknowledging previous work, alternative approaches, and the limitations of current AI capabilities. This helps situate the research contribution and avoids overstating the novelty or significance of the AI-assisted findings.
- Engage in peer review and collaboration with other researchers to validate the methodological soundness and interpretability of the AI-assisted research. Sharing code, data, and detailed methodological descriptions can facilitate this process and help maintain the rigour and reproducibility of the work.
- Validate AI-generated results' accuracy, reliability, and robustness using established statistical methods and domain-specific evaluation criteria. This may involve comparing AI outputs to human-generated benchmarks, conducting sensitivity analyses, or assessing the model's performance on out-of-sample data.
- Provide comprehensive and accessible documentation of the AI methods, assumptions, and limitations to support the credibility and replicability of the research. Be transparent about the limitations of the AI tools and avoid overstating their capabilities or the conclusions that can be drawn from their use.

## Guidelines for the Scientific Testing of AI Capabilities

### Compare to human baselines

- When evaluating an AI's capabilities, compare its performance to human
  benchmarks on the same task. This helps contextualise the AI's performance and provides a meaningful reference point for assessing its strengths and limitations.
- Establish human performance through controlled tests using a sample of people
  with relevant skills and experience. Ensure that the human participants are representative of the intended user population and that the testing conditions are standardised and well-documented.
- Report the performance of both AI and human baselines using the same metrics
  to allow direct comparison. Use widely accepted and domain-specific evaluation metrics to facilitate comparability and reproducibility of the results.

### Test for robustness & reliability

- Evaluate how robust the AI is to changes in input format, wording of instructions, or domain of application. For example, the AI's performance can be tested on different data types, such as structured vs unstructured text, plain text, or markdown formatted text.
- Feed the model edge cases and adversarial examples to identify potential
  failure modes and weaknesses.
- Test the AI on data from different time periods, cultural contexts, and
  demographics to its training set.
- Assess performance across a range of temperatures and other model parameters.
- Assess the AI's performance consistency across multiple runs with the same
  inputs and parameter settings.
- Investigate whether the model exhibits inconsistencies or contradictions in
  its outputs. Design tests that probe for logical inconsistencies, such as asking the AI to reason about equivalent problems framed in different ways.
- Ask the model to assess its confidence in its conclusions where relevant. Treat the AI's confidence scores as a valuable source of information, but critically examine the reasons behind its uncertainty.

### Interrogate decision-making processes

- Probe how the AI arrives at its outputs – look inside the black box as much as
  possible.
- Play with different techniques like zero-shot prompts, few-shot prompts, and
  chain-of-thought prompting to explain the model's reasoning.
- Examine attention weights, activations, and embeddings to gain insight into
  the model's inner workings.
- Conduct controlled experiments that systematically manipulate the input prompts to test the stability and consistency of the AI's reasoning.
- The existence of questions or other content within the model's training data will skew results. As such, it is better to develop original and unbiased test cases that are not likely to be present in the AI's training data to get a more accurate assessment of its actual capabilities.
- Be especially vigilant when the AI generates information about specialised or esoteric domains, as it may be more prone to hallucination or inaccuracy in these areas. Check for
  accuracy and try to determine the source of obscure information returned.

### Acknowledge limitations

- Be clear about the constraints of the testing conditions and domains of
  applicability. Explicitly state any assumptions, limitations, or biases in the testing methodology or data that could affect the generalisability of the results.
- Highlight uncertainties and aspects of the model that are not well understood. Be transparent about any knowledge gaps or open questions regarding the AI's behaviour or capabilities.
- Frame findings as provisional hypotheses rather than definitive conclusions
  about AI capabilities in general. Use cautious and qualified language when interpreting the results, acknowledging that they are specific to the particular AI system and testing conditions.
- Acknowledge that results may not generalise to other models, versions, or
  parameter settings.

### Foster open science

- Where safe, publish all code, data and models to enable replication and
  further research.
- Provide complete and detailed documentation of the AI system and testing methodology to support the reproducibility and comparability of the results.
- Engage in open peer review and solicit feedback from diverse perspectives to identify blind spots and improve the rigour of the research.
- Participate in public discourse and multidisciplinary dialogues to collectively make sense of the findings and their potential societal consequences.

### Examine social and ethical implications

- Consider the potential societal impacts, both positive and negative, of the AI
  capabilities being developed and tested.
- Engage with affected communities and stakeholders to understand their
  perspectives and concerns.
- Create safeguards, guidelines, and governance mechanisms to prevent or respond to unintended consequences and malicious applications of the AI.
- Consider the potential harms associated with publishing the research and the underlying AI technology. Carefully weigh the benefits of open publication against the risks of misuse or exploitation, and consider implementing responsible disclosure practices or access restrictions when necessary.

## Considerations for Using Generative AI in Qualitative Research Methodology

The integration of generative AI into qualitative research methodologies offers
possibilities for data analysis, theme generation, and insight discovery. The
capability of generative AI to carry out "human-level" tasks presents
opportunities to speed up the processing of large quantities of data or
undertake novel approaches to qualitative research. However, the unique nature
of qualitative research, with its emphasis on depth, context, and subjective
interpretation, requires careful consideration of several factors to ensure the
integrity of research outcomes. Below are several key considerations for researchers aiming to incorporate generative AI into their qualitative research methodologies.

### Alignment with research goals and ethics

1. **Purposeful Integration:** Clearly define the role of generative AI in
   qualitative research. Whether it is used for data analysis, generating
   interview questions, or synthesising themes, ensure that its application
   directly supports the research objectives without compromising the depth and
   nuance of the research's proposed outcomes.

2. **Ethical Considerations:** Reflect on the ethical implications of using
   generative AI, especially in relation to participant consent,
   confidentiality, and the potential for bias. Be transparent with participants
   about the use of generative AI in the research process and consider the
   impact of AI-generated insights on the research subjects and broader societal
   contexts.

### Human-AI collaboration and researcher competency

1. **Human-AI Collaboration:** Emphasize the importance of human-AI collaboration in qualitative research. While generative AI can assist in various tasks, it should not replace human judgment, expertise, and contextual understanding. Researchers should work in tandem with AI tools, leveraging their complementary strengths to enhance the quality and depth of the research.

2. **Training and Competency:** Researchers should acquire the necessary technical skills and knowledge to integrate AI into their research workflows effectively. This may involve learning about AI fundamentals, familiarising themselves with specific AI tools and platforms, and staying updated on best practices and ethical guidelines for AI use in research.

### Data integrity and authenticity

1. **Data Handling:** Exercise caution in feeding sensitive or identifiable data
   into generative AI tools. Anonymise data where possible to protect
   participant privacy and comply with data protection regulations.

2. **Authenticity of Insights:** While generative AI can help identify patterns and themes in data, critically evaluating these insights for authenticity and relevance is crucial. Researchers should not rely solely on AI for data interpretation but use it as a tool to complement their analytical skills and subject matter expertise.

3. **Verify Capabilities:** Before undertaking large-scale data processing using generative AI, have it process a representative subset of the data and have a human verify that the AI model is performing as desired. This verification stage should form a key step in the reported methodology and results to demonstrate that the generative AI and the parameters set are verified as performing pursuant to the objectives of its use.

4. **Iterative Analysis:** Employ an iterative approach to data analysis, alternating between generative AI-assisted and traditional manual methods. This hybrid strategy can aid in speeding up the research while ensuring the rigour and depth of the qualitative research are maintained.

### Methodological transparency and reproducibility

1. **Critical Engagement and Reflexivity:** Maintain a reflexive stance towards
   the use of generative AI, continually questioning how it influences the
   research process, the construction of knowledge, and the interpretation of
   data. Acknowledge the limitations of generative AI and the potential for the
   technology to shape research outcomes in unforeseen ways.

### Mitigating bias and acknowledging limitations

1. **Bias Detection and Correction:** Like humans, generative AI is not free from subjective viewpoints. Actively seek to identify, measure and mitigate biases in the generative AI's outputs. This involves critically assessing the data sources, training materials, intended users, and inherent model biases. Employ diverse datasets and consider multiple perspectives to challenge and refine the AI-generated insights. Prompting can be effective in altering, to a degree, the viewpoints expressed by generative AI.

2. **Contextual Sensitivity:** Stress the significance of contextual sensitivity when applying generative AI. Qualitative data often involves nuanced meanings, cultural specificities, and personal narratives that may not be fully captured by AI algorithms. Researchers should be cautious not to over-rely on AI-generated insights and should always interpret the results within the broader context of the research setting.

3. **Diversity of Data and Perspectives:** Ensure that the data fed into generative AI tools and the resulting analysis reflect the diversity of the research population. Be wary of over-generalisation and the erasure of minority experiences and perspectives. At the same time, be aware that the alignment training of generative AI systems may lead to models overrepresenting minority perspectives.

## Responsible Publication and Dissemination

### Consider dual use

- Be mindful that research intended for beneficial purposes may be misused or
  have unintended negative consequences.
- Consider the potential for malicious use of AI capabilities before publishing.
- If necessary, limit the release of code, data or models that could be easily
  abused.

### Engage in public dialogue

- Communicate research findings clearly and accessibly to non-expert audiences.
- Be proactive in engaging with the media, policymakers and the public about the
  implications of the research.
- Correct misconceptions and overhype about AI capabilities.
- Participate in multidisciplinary discussions about the responsible development
  of AI.

### Continuously update practices

- Keep up-to-date with the latest research and evolving best practices for
  responsible AI development.
- Proactively update research practices, transparency measures and ethics
  guidelines as the technology progresses.
- Consult with ethics review boards and AI governance experts as appropriate.
- Contribute to the development of standards and governance frameworks for
  responsible AI.

---

## Disclosure of the use of Generative AI in the Creation of this Document

This document was created with the assistance of the following AI tools.

- [SapienAI](https://academicid.io/sapien): a self-hosted tool of the author's creation. It is a generative AI chatbot powered by various language models, including OpenAI's GPT-4-Turbo and Anthropic's Claude Opus. The tool was primarily used to provide suggestions for overlooked content. For example, the tool was provided with a section draft and asked, `Can you think of any obvious omissions in this section?`. The response to these prompts was then reviewed and incorporated into the document where appropriate.
- [GitHub Copilot](https://copilot.github.com/): an AI-powered code completion tool provided by GitHub. This document was written in [VS Code](https://github.com/features/copilot/) with the Copilot extension enabled. Copilot was used to provide Markdown formatting support.
