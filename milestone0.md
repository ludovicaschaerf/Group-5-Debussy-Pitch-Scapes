# Milestone 0

### Research Question
Debussy played a crucial role in the turning point from the 19th to the 20th century in western music. Many of his works are characterised by innovative sonorities which cannot be associated with functional harmony or tonality. His style emphasizes color, texture and mood, accomplishing a feat of floating and elusive vagueness.

Harmonic analysis of post-tonal music in which diatonicism and experimental sonorities coexist is a complex issue, which often results in different and controversial interpretations.

The aim of this project is to investigate the harmonic construction of Debussy’s piano works, trying to identify the main compositional techniques that he applies to achieve this sense of ambiguity and to find a structural coherence between them. Additionally, through the harmonic analysis of his work, we will trace the gradual shift from clarity of tonality towards tonal ambiguity in Debussy’s piano music.

Among the factors that concur to define Debussy’s harmonic practice, we expect to find:
-scales: whole tone scales, pentatonic scales, modal scales, chromatic scales, octatonic scales
-interval types: whole tone chords(major triads, augmented triads), extended chords, open fourths, fifths and chords without thirds
-harmonic progressions: parallelism, third related progressions, root progressions by step, polytonality, polymodality, unusual dominant resolutions, modal cadences.

We hope to find relevant selections or combinations of these features that convey on a larger scale the different harmonic sections of the pieces and to observe how a weakened sense of motion and tonality arise from them.

### Concepts and Data
In terms of the dataset, we would like to extract the MIDI representation of some of Debussy’s works. We will focus on the piano works which are more experimental in terms of tonal ambiguity, such as Debussy’s Preludes and Images, but we will also consider examples of a more traditional repertoire to make relevant comparisons. 

We believe that scraping this websites https://www.musicxml.com/music-in-musicxml/ and retraining the first n results should suffice. We do not aim at getting ‘big data’ and retrieving all the possible works as the model should not suffer too much from lack of data and we favour the possibility of an in-depth interpretation of our results based on pivotal pieces.  

We will analyse the use of: pitch sets(different scales), interval/chord sets and harmonic progressions. To obtain them, we will parse the scores into units of different sizes, counting the distribution of pitches and the vertical and horizontal intervals between voices and chords. We will also try to combine these concepts with the perspective of Tonfeld theory and identify relevant pitch fields for our analysis. To obtain a hierarchical structure of these features, we will exploit the notion of pitch spaces present in [1].

### Methods
In our project, we would like to mirror the methods introduced in [1]. That is, we would like to generalize over the key structure extraction using pitch scapes to extraction using chord and interval types, harmonic progressions, and scales. In this respect, the process will consist of two steps: First, we need to extract the above concepts from MIDI encoded pieces and encode them (i.e. an option would be to encode interval types into consonant / 1 and dissonant / 0, NB: we will not necessarily opt towards this encoding), of course, another option would be to find already annotated pieces; Secondly, we need to model the Gaussian Mixture of the concepts mentioned above into ‘scapes’ and potentially aggregate them into a single result (i.e. the key scape estimation from pitch scapes in the paper). The results will be shown using triangular scape plots which will allow us to determine whether the expectations we listed out in ‘possible outcomes’ are supported or not by our quantitative analysis.

### Literature
[1] analyzes the harmonic structure based on pitch scapess.
[2] proposes a generative syntax of diatonic harmonic progressions based on linguistic approaches and on the GTTM, modelling a hierarchical harmonic structure.
[3] works on the acoustic signal to find music structure. After analysing the signal, a set of segments are generated as ground truth, the authors construct the music structure by matching the segments in a music piece to the ground truth segments.

[1] Lieck, R., & Rohrmeier, M. (2020). Modelling hierarchical key structure with pitch scapes. In Proceedings of the 21st International Society for Music Information Retrieval Conference, Montréal, Canada.
[2] Rohrmeier, M. (2007). A generative grammar approach to diatonic harmonic structure. In Proceedings of the 4th sound and music computing conference (pp. 97-100).
[3] Paulus, J., & Klapuri, A. (2006, October). Music structure analysis by finding repeated parts. In Proceedings of the 1st ACM workshop on Audio and music computing multimedia (pp. 59-68).

[1, 3] analyze the music structure regarding one aspect of the music, however we aim to build structures based on different features we can extract from the music piece and figure out the relations between different result structures. [2] generates structure for diatonic harmony, but Debussy’s works contain non-tonal and non-functional elements, it would be interesting looking into the structure of such music.

