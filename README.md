# Analyzing Machine Learning Approaches for Phishing Website Detection
Final year project at B.E college

Phishing attacks have become a paramount concern for cybersecurity researchers due to their sophisticated methods of deception, especially in crafting fake websites that closely mimic legitimate ones. 
This mimicry poses a significant challenge as evenm knowledgeable users can struggle to distinguish between authentic and fraudulent sites, making them susceptible to falling prey to phishing attacks. 
The primary objective of these attacks typically revolves around illicitly acquiring sensitive information, with a particular focus on banking credentials, leading to substantial financial losses. For 
instance, businesses in the United States alone report losses of approximately $2 billion annually due to phishing attacks, as indicated in [1]. The global impact, as estimated in the 3rd Microsoft 
Computing Safer Index Report of February 2014, could potentially exceed $5 billion. The success of phishing attacks is often attributed to the lack of user awareness regarding these deceptive practices. 
Since phishing attacks capitalize on exploiting user vulnerabilities, effectively mitigating them proves to be a complex challenge.Nonetheless, enhancing phishing detection techniques is imperative to 
combat this pervasive traditional approach to identifying phishing websites involves updating blacklisted URLs and Internet Protocol (IP) addresses in antivirus databases,commonly referred to as the 
"blacklist" method. However, attackers constantly innovate by employing creative techniques such as URL obfuscation, fast-fluxtechniques with automated proxies, algorithmic generation of new URLs, and 
more, which can effectively evade blacklists. 

Objectives:
The objectives of the research are as follows:

 Develop Machine Learning-Based Defense Mechanisms: 
    The primary objective is to develop and implement machine learning-based defense mechanisms to enhance cybersecurity, specifically focusing on detecting and categorizing phishing websites.
 Utilize Various Approaches for Website Categorization: 
    Explore and utilize various approaches and techniques for categorizing websites based on their URLs. Thisincludes feature extraction methods, machine learning algorithms, and classification techniques.
 Feature Extraction using RFEC Method: 
Implement the Recursive Feature Elimination with Cross-validation (RFEC) method for feature extraction from URLs. RFEC is utilized to identify and select the most relevant features that distinguish between 
legitimate, suspicious, and phishing URLs.
 Implement XG Boost and Gradient Boosting Classifiers: 
    Develop and train machine learning classifiers, specifically XG Boost and Gradient Boosting, to classify websites into categories such as legitimate, suspicious, or phishing. These classifiers are chosen 
for their effectiveness in handling classification tasks.
 Evaluate Classifier Performance: 
    Evaluate the performance of the trained classifiers using a dataset containing real-world URLs. Performance metrics such as accuracy, precision, recall, and F1 score are used to assess the classifiers' 
ability to correctly classify URLs and distinguish between real and fraudulent websites.
 Achieve High Classification Accuracy: 
    The objective is to achieve a high classification accuracy rate, with the classifiers successfully distinguishing between real websites and phishing sites over 90% of the time.
 Contribute to Cybersecurity Enhancement: 
    Ultimately, the research aims to contribute to enhancing cybersecurity measures by providing robust and accurate methods for detecting and categorizing phishing websites. This helps protect users 
fromonline threats and reduces the impact of phishing attacks on individuals and organizations.

Proposed System:

    The aim of this research is to enhance defense mechanisms against phishing attacks by developing and implementing machine learning-based methodsto categorize websites. Specifically, the research 
focuses on utilizing various approaches to classify websites based on their URLs. The methodology includes the development of a system that employs machine learning techniques for website classification, 
with a particular emphasis on feature extraction using the Recursive Feature Elimination with Crossvalidation (RFEC) method. Additionally, two classifiers—XG Boost and Gradient Boosting—are utilized to 
classify websites into categories such as legitimate,suspicious, or phishing sites.

Problem Statement:

    With the exponential growth of online activities, the proliferation of phishing attacks has become a critical cybersecurity concern, posing substantial risks to both individuals and organizations. 
Phishing URLs leverage social engineering tactics, preying on human vulnerabilities in information security awareness to deceive users into accessing fraudulent websites. Traditional security measures, 
including blacklisting and whitelisting, face limitations in keeping pace with the dynamic nature of phishing attacks. To address this challenge, our paper tackles the pressing issue of real-time
website authentication by proposing a robust system for distinguishing between legitimate and fraudulent websites based on their URLs. By analysing URLs in realtime, the framework aims to empower users 
with a proactive defence mechanism, helping them differentiate between genuine and deceptive websites to enhance online security.

Methedology:
    Machine learning based different algorithms were run in the experiment.
	 These are: Random Forest(RF), Naive Bayes (NB), XG Boost, Gradient descent.
XG Boost is an algorithm based on gradient boosted decision trees that put speed and performance in the foreground. 
Naive Bayes is a classification algorithm based on conditional probability. It works according to Bayes' theorem. It is preferred due to its easy implementation and less training time. 
Gradient descent is the most popular optimization strategy used in machine learning and deep learning. 
Random Forest is an algorithm that works with the Ensemble Learning technique by creating a large number of trees in the dataset. It divides into subtrees.

System Architecture:
![image](https://github.com/sahana-devops11/Project-final-year/assets/165457131/6a2229f9-f895-4a98-8b6a-e10905fd6b34)

Use Case Diagram:
![image](https://github.com/sahana-devops11/Project-final-year/assets/165457131/cc5436a6-06f6-4a9d-9b14-89a5046615e8)

Activity Diagram:
![image](https://github.com/sahana-devops11/Project-final-year/assets/165457131/c724c443-d7f4-42fe-97cf-6d8bc1b0487f)

Sequence Diagram:
![image](https://github.com/sahana-devops11/Project-final-year/assets/165457131/49dc33a6-eb5d-4446-a532-e5791e73ff27)

Test Cases:
![image](https://github.com/sahana-devops11/Project-final-year/assets/165457131/36419583-d466-453f-92c1-968d18b11a2b)

   
