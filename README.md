# Fake News Classification using DistilBERT

**Authors:**  
Kevin Peng, Malak Soubai, Arden Feldt, Murad Abdi, Christopher Vasquez, Dasha Tran  
**Institution:** University of North Carolina at Chapel Hill (COMP 560)  
**Address:** 232 S Columbia St, Chapel Hill, NC 27514  
**Emails:** kevpeng@unc.edu, smalak@unc.edu, feldt@unc.edu, cjvasque@ad.unc.edu, dashatr@email.unc.edu  

---

## Abstract

We propose a machine-learning model fine-tuned based upon the training data of real versus fake news, specifically derived from the existing DistilBERT encoder-only model. Such techniques can be trained to be used upon a variety of input information, including article text, article title, and article source. We present two case studies to show how supervised fine-tuning (SFT) can be used upon article text and article titles to assess the validity of potential news sources.

**Keywords:** Fake News, DistilBERT, Encoder-only Model, Transformers, Machine Learning Techniques, Supervised Fine-Tuning

---

## 1. Introduction (Motivation + Why this tech?)

Fake news is defined as a story that is false, fabricated, or unverified [1]. With the widespread availability of digital content and the rise of networking websites, information is highly accessible today, with 88% of fake news found on social media platforms [2]. In the USA, 38.2% of people accidentally share fake news, which becomes a pressing challenge [3]. 

In this paper, we explore the use of artificial intelligence for detecting fake news. Specifically, we utilize a text classification method, DistilBERT, a transformer model based on the BERT architecture that is optimized for speed and accuracy [4]. We trained our model using a dataset from Kaggle, consisting of article titles, article text, and labels marking the news as real or fake. 

Through our work, we aim to contribute to the development of electronic communication and flag misleading content to promote a more informed society and protect the integrity of digital information.

---

## 2. Process

### 2.1 Technology Intro

In this paper, we present a use case of encoder-only transformer models. Encoder-only transformers tokenize a variety of supplied input texts, then pass the ensuing values into the encoding layers. The final transformer layer outputs a single classifier label; in our use case, it simply represents the expected truthfulness of the given input: `1.0 = false news`, `0.0 = true news`.

### 2.2 Preparing Datasets

In our search for fake news-related datasets, we narrowed the list to seven options. Initially, we used a dataset with 40,000+ entries [5], combining the fake and true news CSV files, labeling them with 1s and 0s, and splitting the dataset for training.

However, this dataset had an issue: most articles were from just a few organizations, making it easy for the model to learn to classify based on the publisher rather than content.

We then switched to a better dataset from Kaggle [6] with over 60,000 unique entries and only four relevant columns: Index, Title, Text, Label. We trained on both `Title` and `Text`, using the `Label` for classification.

We used the Kagglehub library to download the data and a Python script to randomize and split the dataset (80% training, 20% testing). The data was uploaded to [Hugging Face Datasets](https://huggingface.co/datasets/Feldt/NewCombined) for team-wide access due to file size constraints.

### 2.3 Training

We experimented with two approaches:

- Using **article titles** only  
- Using **article text** only  

The base DistilBERT model was downloaded from [Hugging Face](https://huggingface.co/docs/transformers/en/model_doc/distilbert) and fine-tuned with our Kaggle datasets.

#### 2.3.1 Initial Training (Bad Dataset)

True and fake news had noticeable formatting differences (e.g., real news used capitalized locations like "WASHINGTON"), allowing the model to easily classify based on formatting instead of content. This yielded an unreasonably high accuracy of 99.8%, but it wasn’t representative of real-world performance.

#### 2.3.2 Next Training

Using the improved dataset, we trained two models: one on **titles only**, and another on **text only**, using the same labels for both. Each model was trained for 2 epochs.

---

## 3. Results and Conclusion

### 3.1 Initial Training (Bad Dataset)

- **Accuracy:** 99.8%  
- **Problem:** Model learned to classify based on formatting quirks, not meaningful content.

### 3.2 Next Training

- **Title-only model accuracy:** 95.6%  
- **Text-only model accuracy:** 99.4%  

Both models showed strong performance, with the text-based model slightly outperforming the title-based one in accuracy, though requiring more computation.

### 3.3 Conclusion

Supervised fine-tuning with DistilBERT provides promising results in fake news classification. Both the title-only and text-only models achieved over 95% accuracy. Title-only models offer a lightweight option, while text-only models provide higher accuracy at a higher computational cost. Both approaches are viable and deserve further exploration.

---

## References

1. Desai, S., & Oehrli, J. A. (2023). ["Fake News," Lies and Propaganda](https://guides.lib.umich.edu/fakenews). University of Michigan.  
2. Beauvais, C. (2022). [Fake news: Why do we believe it?](https://pmc.ncbi.nlm.nih.gov/articles/PMC9548403/)  
3. Watson, A. (2024). [Frequency of seeing false news online U.S. by age 2023](https://www.statista.com/statistics/1462057/false-news-consumption-frequency-us-by-age/)  
4. [DistilBERT Overview](https://www.sciencedirect.com/topics/computer-science/distilbert)  
5. [Fake and Real News Dataset (clmentbisaillon)](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset)  
6. [Fake News Classification Dataset (Shahane)](https://www.kaggle.com/datasets/saurabhshahane/fake-news-classification)  
7. [GitHub: comp560finalproject](https://github.com/Arden-Feldt/Comp560FinalProject)  
8. [Hugging Face Dataset: NewCombined](https://huggingface.co/datasets/Feldt/NewCombined)  
9. [Hugging Face Model: DistilBERT](https://huggingface.co/docs/transformers/en/model_doc/distilbert)

---

## Additional Reading (Not Linked in Body)

- [Text Classification - Hugging Face](https://huggingface.co/docs/transformers/en/tasks/sequence_classification)  
- Pennycook, G., et al. (2018). [Prior exposure increases perceived accuracy of fake news](https://doi.org/10.1037/xge0000465)  
- [DistilBERT Explained - Papers With Code](https://paperswithcode.com/method/distillbert)  
- Tripathy, J. K., et al. (2021). [Comprehensive analysis of embeddings and pre-training in NLP](https://doi.org/10.1016/j.cosrev.2021.100433)

---

## Models

- [Article Text Only Model](https://huggingface.co/kpeng-05/Fake-News-Detection-2.0-Text)
- [Article Title Only Model](https://huggingface.co/kpeng-05/Fake-News-Detection-2.0-Title)
