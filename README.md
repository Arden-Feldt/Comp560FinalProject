# Comp560FinalProject
## AI in Detecting Fake News 

## Abstract 
We will be exploring the use of various reinforcement learning from human feedback-based models from different applications, including Kahneman-Tversky Optimization (KTO), Direct Preference Optimization (DPO), and Reinforcement Learning with Human Feedback (RLHF), in the use of detecting misinformation and fake news.

## Application
In a moment where more and more information online is misleading or fictitious, a tool to help readers discern honest reporting from social media slop would be greatly beneficial. However, a computer’s ability to detect bots or factually inaccurate media is often still behind that of humans currently and could use the extra information from human readers to notice and flag misinformation. Many online social media platforms already offer the option to label posts as “misleading” or “spam” from users, and this extra human input could create a boost in a model’s ability to detect potential misinformation.

## Data
There are [datasets](https://www.kaggle.com/datasets/khushikyad001/fake-news-detection) that we plan to train on. Connecting the contents (full_text) of an article to ‘honesty’ metrics included in the dataset, like the stories' trust_score, political_bias, and fact_check_ranking, is a powerful way for us to predict if stories are disingenuous. For the training of the RLHF models, we plan on adding additional human data that represents how humans would perceive the truthfulness of the information.

## Methodology
We plan on implementing the reinforcement learning training based on preexisting transformer models from Huggingface, and testing the altered models’ accuracy with the ground truth, especially when compared to a similar model without the extra help of human input.

