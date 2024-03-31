# Responsible AI in Academia

**Author:** _Kieran Lindsay_ | **First published:** March 31, 2024 | **Last
update:** March 31, 2024 _(see file history for versions)_

---

These are some preliminary guidance principles that can be followed when using
generative AI to assist with your research and where generative AI forms the
subject of your research.

The use of generative AI in research is not inherently bad practice. In fact, it
has the potential to accelerate and enrich many aspects of the research process,
from hypothesis generation to data analysis to dissemination. However, to ensure
the reproducibility and integrity of research that involves generative AI, it is
vital to be transparent about its use.

We're still learning about the impact of these different technologies and the
vast configuration options already available to us. As such, it's extremely
important to be transparent and specific about the use of and exact setup used
(e.g. models used, prompts, etc.) and explore how varying them affects
performance.

Including these details in write-ups and open datasets will help the community
build a clearer picture of AI capabilities and move the field forward. It's an
exciting time for AI research but also one where we need to be thoughtful about
our methods and transparent in our reporting.

These guidelines are preliminary and are being expanded on. These should not be
relied on solely but used in conjunction with established research procedures,
best practices, methodologies and ethics guidelines.

## Guidelines for Using Generative AI to Assist Academic Research

1. **Transparency and disclosure**

- Always disclose when generative AI has been used to assist with any part of
  the research process, from ideation to data analysis to writing. This should
  be noted in the methodology section.
- Describe how the AI was used - e.g. brainstorming ideas, literature searches,
  data coding, writing sections of the paper, etc.
- Specify dates and which AI tools or models were used (e.g. ChatGPT, DALL-E
  etc).
- Ensure prompts used and any system prompts are documented.
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
  altered.

2. **Human oversight and editorial control**

- While AI can assist various stages of research, final decisions, analysis, and
  write-up should be human-led.
- Carefully fact-check and validate any AI-generated content. Do not assume it
  is accurate.
- Maintain editorial control - a human researcher should always have the final
  say over a paper's content and conclusions.

3. **Respect intellectual property**

- Be cautious about AI reproducing copyrighted text or images in its outputs.
- If using AI-generated content, ensure it is sufficiently original and distinct
  from its training data.

4. **Consider research ethics**

- Using AI does not circumvent standard research ethics protocols. Studies still
  require ethics approval where applicable.
- Take steps to remove personally identifying information from data before
  feeding it to an AI system.
- Consider potential negative impacts or unintended consequences of the research
  as a result of AI usage, such as bias or over-reliance by involved
  researchers.

5. **Reproducibility and data availability**

- Aim to use open-source AI models where possible to aid reproducibility.
- Share code, data and methodology to allow other researchers to verify and
  build upon the work.
- Archive versioned copies of AI models or datasets used, as these can change
  over time.
- Ensure any AI-generated content can be reproduced by specifying the exact
  prompts, model and parameters used.

6. **Mitigate bias**

- Be aware that AI models can reflect biases present in their training data,
  which may lead to biased outputs.
- Take steps to identify and mitigate potential biases, such as testing the
  model on diverse datasets and examining outputs for stereotyping or unequal
  treatment.
- Consider the societal impact and potential for discrimination arising from the
  use of the AI model.

7. **Maintain academic standards**

- The use of AI should not compromise the research's quality, rigour, or
  integrity.
- AI-assisted work should still meet field-specific standards for methodology,
  evidence, and argumentation.
- Be transparent about the limitations of the AI tools and avoid overstating
  their capabilities or the conclusions that can be drawn from their use.

## Guidelines for Scientific Testing of AI Capabilities

1. **Compare to human baselines**

- When evaluating an AI's capabilities, compare its performance to human
  benchmarks on the same task.
- Establish human performance through controlled tests using a sample of people
  with relevant skills and experience.
- Report the performance of both AI and human baselines using the same metrics
  to allow direct comparison.

2. **Test for robustness & reliability**

- Evaluate how robust the AI is to changes in input format, wording of
  instructions, or domain of application.
- Feed the model edge cases and adversarial examples to identify potential
  failure modes and weaknesses.
- Test the AI on data from different time periods, cultural contexts, and
  demographics to its training set.
- Assess performance across a range of temperatures and other model parameters.
- Assess the consistency of the AI's performance across multiple runs with the
  same inputs and parameter settings.
- Investigate whether the model exhibits inconsistencies or contradictions in
  its outputs.
- Evaluate the AI's calibration - the extent to which its confidence scores
  align with its actual accuracy.

3. **Interrogate decision-making processes**

- Probe how the AI arrives at its outputs - look inside the black box as much as
  possible.
- Use techniques like zero-shot prompts, few-shot prompts, and chain-of-thought
  prompting to elucidate the model's reasoning.
- Examine attention weights, neuron activations, and embeddings to gain insight
  into the model's inner workings.
- Vary prompts and instructions to see how this changes the model's outputs and
  apparent reasoning.
  - The existence of prompts (e.g. questions being asked) within the training
    data will skew results compared to novel questions, regardless of whether
    the semantic meanings are similar.
- Pay close attention and interrogate output relating to niche topics. Check for
  accuracy and try to determine the source of obscure information returned.

4. **Acknowledge limitations**

- Be clear about the constraints of the testing conditions and domains of
  applicability.
- Highlight uncertainties and aspects of the model that are not well understood.
- Frame findings as provisional hypotheses rather than definitive conclusions
  about AI capabilities in general.
- Acknowledge that results may not generalise to other models, versions, or
  parameter settings.

5. **Foster open science**

- Where safe, publish all code, data and models to enable replication and
  further research.
- Include details of model versions and parameters used in any public write-ups
  or datasets.
- Proactively invite scrutiny from the wider research community.
- Engage in open debate about the interpretation of results and their real-world
  implications.

6. **Examine social and ethical implications**

- Consider the potential societal impacts, both positive and negative, of the AI
  capabilities being developed and tested.
- Engage with affected communities and stakeholders to understand their
  perspectives and concerns.
- Develop mitigation strategies for potential harms or misuse of the technology.
- Consider the potential harms associated with publishing the research and/or
  the underlying AI technology.

## Responsible Publication and Dissemination

1. **Consider dual use**

- Be mindful that research intended for beneficial purposes may be misused or
  have unintended negative consequences.
- Consider the potential for malicious use of AI capabilities before publishing.
- If necessary, limit the release of code, data or models that could be easily
  abused.

2. **Engage in public dialogue**

- Communicate research findings clearly and accessibly to non-expert audiences.
- Be proactive in engaging with the media, policymakers and the public about the
  implications of the research.
- Correct misconceptions and overhype about AI capabilities.
- Participate in multidisciplinary discussions about the responsible development
  of AI.

3. **Continuously update practices**

- Keep up-to-date with the latest research and evolving best practices for
  responsible AI development.
- Proactively update research practices, transparency measures and ethics
  guidelines as the technology progresses.
- Consult with ethics review boards and AI governance experts as appropriate.
- Contribute to the development of standards and governance frameworks for
  responsible AI.
