# Responsible AI in Academia

**Author:** _Kieran Lindsay_ (ORCID: 0000-0002-1624-7679) | **First published:**
March 31, 2024 | **Last update:** April 29, 2024 _(see file history for
versions)_

_This is a living document. It is open source, and anyone is welcome to make
suggestions. You can find the source and document history
[here](https://github.com/Academic-ID/academicAI) or reach out to Kieran at
kieran@academicid.net_

---

Below are some preliminary guidance principles that academics, researchers and
students can follow when using generative AI to assist with their research or in
situations where generative AI forms the subject of their research.

The use of generative AI in research is not inherently bad practice. In fact, it
has the potential to accelerate and enrich many aspects of the research process,
from hypothesis generation to data analysis to dissemination. However, to ensure
the reproducibility and integrity of research that involves or utilises
generative AI, it is vital to be transparent about its use.

We are still learning about the impact of these different technologies and the
vast configuration options already available to users. As such, it is essential
that users of this technology are transparent and specific about the use of
generative AI.

Including details on AI use and specific details on models and parameters
utilised will help the community build a clearer picture of AI capabilities and
move the field forward. It is an exciting time for AI research and the use of AI
in research.

These guidelines are preliminary and are being incrementally expanded and
improved. As such, these should not be relied on solely but used in conjunction
with established research procedures, best practices, methodologies and ethics
guidelines.

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

1. **Bias and Fairness:** Generative AI systems, reflecting biases in their
   training data, can perpetuate or exacerbate societal biases. This risk is
   particularly concerning in research applications that impact decision-making
   in critical areas such as healthcare, justice, and employment or the use of
   generative in qualitative or research methodologies involving any degree of
   subjective assessment. For instance, a generative AI model trained on
   historical medical data might inherit biases against certain demographic
   groups, leading to skewed research outcomes that reinforce health
   disparities. It is vital to remember that companies train large language
   models for performance, safety and alignment, not necessarily balance, and it
   is up to these companies to determine what alignment is.

2. **Privacy Concerns:** The use of generative AI in processing and synthesising
   data can inadvertently lead to privacy breaches, especially when dealing with
   sensitive or personal information. The ability of these systems to generate
   detailed synthetic data based on real-world datasets poses a risk of
   re-identification of individuals whose data has inadvertently entered the
   training set. Further, even when data is not used for model retraining,
   sending sensitive information to third-party companies may breach contractual
   or legislative privacy provisions.

3. **Intellectual Property and Plagiarism:** Generative AI's capacity to produce
   content that closely mimics existing copyrighted material raises concerns
   about unintentional plagiarism and the violation of intellectual property
   rights. While legally, this remains a grey area, the concern remains
   particularly problematic in academic settings where the originality of
   research outputs is paramount.

### Operational Risks

1. **Reliability and Reproducibility:** The stochastic nature of generative AI
   models means that they can produce inconsistent results, challenging the
   reproducibility of research findings. This variability, coupled with the
   'black box' nature of many AI systems, can make it difficult to understand
   and explain how specific results were generated, undermining research's
   reproducibility, credibility and integrity.

2. **Overreliance and Skill Degradation:** The convenience and efficiency of
   generative AI tools can lead to an overreliance on automated systems,
   potentially atrophying critical research skills such as literature review,
   data analysis, and even the formulation of research questions. This
   overreliance could also lead to researchers accepting AI-generated insights
   without sufficient scrutiny, increasing the risk of propagating errors or
   flawed analyses.

3. **Writing Style and Quality** This risk of overreliance extends to the use of
   generative AI for writing published academic material. Whilst anecdotal, most
   proficient in English will readily question text that uses overly verbose,
   archaic or unneedingly positive language. In addition to the style models are
   trained to mimic, most generative AI models have some form of
   `frequency/presence penalty` that discourages the repeated use of the same
   tokens (words) within close proximity, resulting in an expanded vocabulary
   that is not always warranted. While the impact on style, readability and
   substance are obvious, these may be forgiven, to an extent, for the
   time-saving benefit. However, when content is purported to be human-written,
   drops in quality _may_ result in a feedback loop amplifying these
   deficiencies as models are retrained on this "human-generated" content.

4. **Regulatory and Legal Risks:** The rapid improvement in capabilities of
   generative AI and its applications can outpace existing legal and regulatory
   frameworks, leading to uncertainties and potential non-compliance. For
   example, the deployment of generative AI in healthcare research must navigate
   complex regulations concerning patient data and medical ethics, where
   non-compliance can have significant legal and reputational repercussions.
   Further, and more generally, while it may be tempting to copy any and all
   data into ChatGPT to have it summarised, and even if the risk of this data
   being regurgitated if used to retrain the model is low, sending this data to
   a third party company (potentially out of your jurisdiction) may be a breach
   of contract or privacy-focused legislation.

## Guidelines for Using Generative AI to Assist Academic Research

Now that we know some of the risks associated with generative AI use, it is
important to consider how we can mitigate these risks. Using generative AI in a
manner consistent with ethical and legal obligations is not complicated;
however, it does require some thought. Below are some guidelines for best
practices that will serve as a starting point for the ethical and responsible
use of AI in academic settings. These guidelines are not exhaustive and should
be applied with a level of discretion aligning with the user's comfort with the
technology; additional considerations should be incorporated based on the
identified risks and the specific use case.

### Transparency and disclosure

- Always disclose when generative AI has been used to assist with any part of
  the research process, from ideation to data analysis to writing. This should
  be noted in the methodology section.
- Describe how the AI was used - e.g. brainstorming ideas, literature searches,
  data coding, writing sections of the paper, etc.
- Specify dates and which AI tools or models were used (e.g. ChatGPT, DALL-E,
  etc).
- Ensure all prompts used and any system prompts are documented.
- If knowledge is provided to the large language model (LLM), i.e. in the form
  of uploaded documents or other
  [RAG](https://blogs.nvidia.com/blog/what-is-retrieval-augmented-generation/)
  implementations, make sure this, too, is documented.
  - It may not be feasible or even possible to document all knowledge,
    especially where you may not be aware of the knowledge being provided to the
    LLM as part of the AI system. It is sufficient to record this as
    comprehensibly as possible.
  - For example, if using a chat tool that provides paper titles and abstracts
    from Semantic Scholar to the LLM, you may record the name of the tool, the
    dates it was used, the prompts and other details as per these guidelines,
    and a note stating that AI-generated responses are augmented with academic
    paper titles and abstracts sourced from Semantic Scholar.
- When using customisable solutions, such as AI playgrounds or API endpoints,
  report the exact model version, temperature setting, and any other parameters
  altered. Being aware of these parameters should be a minimum requirement for
  any use of generative AI as part of research methodology or when testing
  generative AI as part of your research. As such, using programmatic solutions
  or customisable playgrounds should be preferred over user interfaces such as
  ChatGPT, where these parameters are not always public and are likely to change
  (e.g., in the event of AB testing by OpenAI).

### Human oversight and editorial control

- While AI can assist various stages of research, final decisions, analysis, and
  write-up should be human-led.
- Carefully fact-check and validate any AI-generated content. Do not assume it
  is accurate.
- Maintain editorial control – a human researcher should always have the final
  say over a paper's content and conclusions.

### Respect intellectual property

- Be cautious about AI reproducing copyrighted text or images in its outputs.
- If using AI-generated content, to the extent possible, ensure it is
  sufficiently original and distinct from its training data.

### Consider research ethics

- Using AI does not circumvent standard research ethics protocols. Studies still
  require ethics approval where applicable.
- Take steps to remove personally identifying information from data before
  feeding it to an AI system.
- Consider potential negative impacts or unintended consequences of the research
  as a result of AI usage, such as bias or over-reliance by involved
  researchers.

### Reproducibility and data availability

- Aim to use open-source AI models where possible to aid reproducibility.
- Share code, data and methodology to allow other researchers to verify and
  build upon the work.
- Archive versioned copies of AI models or datasets used, as these can change
  over time.
- Ensure any AI-generated content can be reproduced by specifying the exact
  prompts, model and parameters used. As noted above, these parameters must be
  controlled and reported for research that others may want to reproduce.

### Mitigate bias

- Be aware that AI models can reflect biases present in their training data,
  which may lead to biased outputs.
- Take steps to identify and mitigate potential biases, such as testing the
  model on diverse datasets and examining outputs for stereotyping or unequal
  treatment.
- Consider the societal impact and potential for discrimination arising from the
  use of the AI model.

### Maintain academic standards

- The use of AI should not compromise the research's quality, rigour, or
  integrity.
- AI-assisted work should still meet field-specific standards for methodology,
  evidence, and argumentation.
- Be transparent about the limitations of the AI tools and avoid overstating
  their capabilities or the conclusions that can be drawn from their use.

## Guidelines for Scientific Testing of AI Capabilities

### Compare to human baselines

- When evaluating an AI's capabilities, compare its performance to human
  benchmarks on the same task.
- Establish human performance through controlled tests using a sample of people
  with relevant skills and experience.
- Report the performance of both AI and human baselines using the same metrics
  to allow direct comparison.

### Test for robustness & reliability

- Evaluate how robust the AI is to changes in input format, wording of
  instructions, or domain of application.
- Feed the model edge cases and adversarial examples to identify potential
  failure modes and weaknesses.
- Test the AI on data from different time periods, cultural contexts, and
  demographics to its training set.
- Assess performance across a range of temperatures and other model parameters.
- Assess the AI's performance consistency across multiple runs with the same
  inputs and parameter settings.
- Investigate whether the model exhibits inconsistencies or contradictions in
  its outputs.
- Evaluate the AI's calibration - the extent to which its confidence scores
  align with its actual accuracy.
- Utilise function/tool calling capabilities where possible. This will aid in
  receiving responses in a standardised format with lower chances of extraneous
  text being returned.
- Ask the model to assess its confidence in its conclusions where relevant –
  make sure to review lower-confidence responses.

### Interrogate decision-making processes

- Probe how the AI arrives at its outputs - look inside the black box as much as
  possible.
- Play with different techniques like zero-shot prompts, few-shot prompts, and
  chain-of-thought prompting to explain the model's reasoning.
- Examine attention weights, activations, and embeddings to gain insight into
  the model's inner workings.
- Vary prompts and instructions to see how this changes the model's outputs and
  apparent reasoning.
- The existence of questions or other content within the model's training data
  will skew results. As such, it is better to formulate novel questions or
  scenarios measuring the same thing instead of using existing ones.
- Pay close attention and interrogate output relating to niche topics. Check for
  accuracy and try to determine the source of obscure information returned.

### Acknowledge limitations

- Be clear about the constraints of the testing conditions and domains of
  applicability.
- Highlight uncertainties and aspects of the model that are not well understood.
- Frame findings as provisional hypotheses rather than definitive conclusions
  about AI capabilities in general.
- Acknowledge that results may not generalise to other models, versions, or
  parameter settings.

### Foster open science

- Where safe, publish all code, data and models to enable replication and
  further research.
- Include details of model versions and parameters used in any public write-ups
  or datasets.
- Proactively invite scrutiny from the broader research community.
- Engage in open debate about the interpretation of results and their real-world
  implications.

### Examine social and ethical implications

- Consider the potential societal impacts, both positive and negative, of the AI
  capabilities being developed and tested.
- Engage with affected communities and stakeholders to understand their
  perspectives and concerns.
- Develop mitigation strategies for potential harms or misuse of the technology.
- Consider the potential harms associated with publishing the research and/or
  the underlying AI technology.

## Considerations for Using Generative AI in Qualitative Research Methodology

The integration of generative AI into qualitative research methodologies offers
possibilities for data analysis, theme generation, and insight discovery. The
capability of generative AI to carry out "human-level" tasks presents
opportunities to speed up the processing of large quantities of data or
undertake novel approaches to qualitative research. However, the unique nature
of qualitative research, with its emphasis on depth, context, and subjective
interpretation, requires careful consideration of several factors to ensure the
integrity and richness of research outcomes. Below are several key
considerations for researchers aiming to incorporate generative AI into their
qualitative research methodologies.

### Alignment with Research Goals and Ethics

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

### Data Integrity and Authenticity

1. **Data Handling:** Exercise caution in feeding sensitive or identifiable data
   into generative AI tools. Anonymize data where possible to protect
   participant privacy and comply with data protection regulations.

2. **Authenticity of Insights:** While generative AI can help identify patterns
   and themes in data, it is crucial to critically evaluate these insights for
   authenticity and relevance. Researchers should not rely solely on AI for data
   interpretation but use it as a tool to complement their analytical skills and
   subject matter expertise.

3. **Verify Capabilities:** Before undertaking large-scale data processing using
   generative AI, have it process a representative subset of the data and have a
   human verify that the AI model is performing as desired. This verification
   stage should form a key step in the reported methodology and results to
   demonstrate that the generative AI and the parameters set are verified as
   performing pursuant to the objectives of its use.

4. **Iterative Analysis:** Employ an iterative approach to data analysis,
   alternating between generative AI-assisted and traditional manual methods.
   This hybrid strategy can enrich the analysis, facilitate the discovery of
   nuanced insights, and ensure the rigor and depth of the qualitative research
   are maintained.

### Methodological Transparency and Reproducibility

1. **Critical Engagement and Reflexivity:** Maintain a reflexive stance towards
   the use of generative AI, continually questioning how it influences the
   research process, the construction of knowledge, and the interpretation of
   data. Acknowledge the limitations of generative AI and the potential for the
   technology to shape research outcomes in unforeseen ways.

### Mitigating Bias and Ensuring Diversity

1. **Bias Detection and Correction:** Like humans, generative AI is not free
   from subjective viewpoints. Actively seek to identify, measure and mitigate
   biases in the generative AI's outputs. This involves critically assessing the
   data sources, training materials, and inherent model biases. Employ diverse
   datasets and consider multiple perspectives to challenge and refine the
   AI-generated insights. Prompting can be effective in altering, to a degree,
   the viewpoints expressed by generative AI.

2. **Diversity of Data and Perspectives:** Ensure that the data fed into
   generative AI tools and the resulting analysis reflect the diversity of the
   research population. Be wary of over-generalisation and the erasure of
   minority experiences and perspectives. At the same time, be aware that the
   alignment training of generative AI systems may lead to models
   overrepresenting minority perspectives.

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
