# Milestone 0

### Research Question
Debussy played a crucial role in the turning point from the 19th to the 20th century in Western music. Many of his works are characterized by innovative sonorities which cannot be associated with functional harmony or tonality. His style emphasizes color, texture and mood, accomplishing a feat of floating and elusive vagueness. [0]
Throughout the 20th century, musicians have indeed recognized Debussy's contribution to compositional practice with the development of several new techniques that constitute an important change in the essence of pitch structuring. Hallmarks of his harmonic style [1] are: 
-scales: whole tone scales, pentatonic scales, modal scales, unusual scales, chromatic scales, octatonic scales
-interval types: whole tone chords(major triads, augmented triads), extended chords, open fourths, fifths and chords without thirds
-harmonic progressions: parallelism, third related progressions, root progressions by step, polytonality, polymodality, unusual dominant resolutions, modal cadences.

Considering tonality as a “system for interpreting pitches or chords through their relationship to a reference pitch (tonic)” (Huron, 2006: 143), many scholars attribute to these practices the destabilization of a unifying referential tonic in Debussy’s music [1,2].
According to Salzmari E. [3], Debussy was the first composer to successfully put forward an alternative to the traditional paradigm, a musical thought based on symmetrical patterns and structures with a highly weakened directional motion and thus a very ambiguous sense of tonal organization. Moreover, Leydon R.V.[4], describes “Debussyism” by illustrating some of the aforementioned techniques, stating:

>“Debussy's saturation of the musical surface with such devices radically undermines unitary tonal identity. Their aim is to complicate the binary oppositions of tension and >resolution, structure and ornament, departure and return, consonance and dissonance oppositions which are defining characteristics of the tonal idiom. Yet while Debussy >certainly obscures functional tonality, he does not entirely abandon it either“

Debussy’s harmonic practice can be positioned midway in the spectrum between extended tonality and extreme atonality, which often leads to controversial interpretations. Considering the broader context of this research, analysis of this kind of music has indeed tended to privilege either Shenkerian paradigms[5] or atonal pitch-class set theory[6], while fewer are the attempts to overcome this traditional division.[4,7]
Being this music neither exclusively tonal or atonal, we want to examine how, in absence of a unifying tonal framework, harmonic structural coherence arises from seeming discontinuities and in which ways the techniques mentioned above account for the impression of ‘weightlessness', ‘statis’[8] and ‘tonal ambiguity’ that many scholars identify. 

We will investigate in particular the harmonic construction of Debussy’s piano music, observing the main compositional frameworks exploited by the composer and tracing the gradual shift from clarity of tonality towards tonal ambiguity in his works.
Observing the development of Debussy’s harmonic practice through our analysis, we expect to find an increase of the exploitation of the techniques precedently described over time and to find some recurrent patterns that characterize his personal way of ‘rearranging familiar and unusual sonorities’ [4].


### Concepts and Data
Using the DFT coefficients and the concept of wavescapes as explained in the Methods section, we will analyze the usage of pitch sets(different scales) and interval/chord sets, identifying sections and hierarchies of the pieces. Through this analysis, we will be able to observe the harmonic progressions present in those pieces.

In terms of the dataset, we would like to extract the MIDI representation of some of Debussy’s works, collecting the MIDI files from this website http://www.kunstderfuge.com/debussy.htm.
We will focus on the piano works which are commonly considered as the most representative of his reaction to tonal harmony [1], such as his Etampes, Preludes and Images, but we will also examine examples of a more traditional repertoire to make relevant comparisons. In general, we will ensure to have a good temporal coverage through our selections, so that we can investigate the evolution of his music.
If needed, we will annotate some scores manually to verify the reliability of the data and provide the ground truth of those pieces.


### Methods
In our project, we plan to use an interplay of manual and automatic work. In terms of the latter, we will use Discrete Fourier Transform (DFT) on MIDI scores to plot wavescapes (from Masters’ thesis provided). This method allows detecting tonal structures hierarchically on the musical piece.
Differently from keyscapes, the detection is extended to non-diatonic scales. This is useful for our project as we expect Debussy to make large use of non-traditional (with respect to functional harmony) intervals and scales. DFT performs the extraction of regular collections of pitch classes. It does so by decomposing the original score signal into sinusoidal waves, each with varying amplitudes and phases. Furthermore, each wave was given a musical interpretation: most of them represent specific chord/scale types [9].
With this method, we plan to close-read some pieces of interest, investigating the structure of their harmony through the identification of sections based on the detected chords and scales. We will then interpret the found sections to find harmonic progressions and discuss whether the detected features raise a sense of ‘stasis’ or ‘tonal ambiguity’.
Additionally, if manageable, we plan to extract other chord types and progressions tweaking the method itself. For instance, we will look at what frequencies might identify extended chords, open fourths, fifths and chords without thirds using the methodology explained in the Masters’ thesis’ section 2.3. 

For the evaluation, we will manually annotate on musescore a subsample of the data into the found scales and harmonic progressions and compare the annotations with the DFT results. We will also manually annotate all progressions and intervals that we cannot reliably extract using DFT. 

With the results of the DFT and the manual annotations, we will plot the features we identify as the most characterizing of the composer’s harmonic practice and the ones possibly establishing ‘tonal ambiguity’. The evaluation of these features will be based on the recurrence of appearance of the extracted chords, scales, or progressions in the pieces. Through this recurrence, we will distant-read the pieces by plotting over time. This will allow us to assess the temporal progression of the composer’s style.



### Literature
[0] Jameson, E.R. (1942). A Stylistic Analysis of the Piano Works of Debussy and Ravel. Thesis presented to the University of north Texas for the Master of Music.

[1] Uchida, R. (1990). Tonal Ambiguity in Debussy's Piano Works. Thesis presented to the school of music of the university of Oregon.

[2] Marcus, D.J. (2009). Inconstant tonality in Debussy's La mer. Dissertation Submitted to the Graduate Faculty of the University of Georgia.

[3]  Salzman, E. (1974). Twentieth-Century Music; An Introduction, p.22 (2nd edition). Published by Prentice-Hall, Englewood Cliffs

[4] Leydon, R.V. (1996). Narrative strategies and Debussy's late style. McGill University
[5] Brown, M. (1993). Tonality and Form in Debussy's Prélude à l'après-midi d'un faune. Music Theory Spectrum 15 Vol. 2. pp 127-143. Published by the Society for Music Theory, Inc.
[6] Forte A. (1991). Debussy and the Octatonic. Music Analysis, Vol. 10 No. 1/2 pp 125- 169. Published by Wiley.
[7] Parks R.S. (1989). The Music of Claude Debussy. Music and Letters, Vol.72 No.1, pp 144-149. Published by Oxford University Press.
[8] Wenk, A. (1983). Claude Debussy and twentieth-century music (Twayne’s Music Series). Twayne Publishers. 

[9] Yust, J. (2015). Schubert’s harmonic language and Fourier phase space. Journal of Music Theory, 59(1), pp 121-181.

[10] Lieck, R., & Rohrmeier, M. (2020). Modelling hierarchical key structure with pitch scapes. In Proceedings of the 21st International Society for Music Information Retrieval Conference, Montréal, Canada.

[11] Rohrmeier, M. (2007). A generative grammar approach to diatonic harmonic structure. In Proceedings of the 4th sound and music computing conference (pp. 97-100).

[12] Paulus, J., & Klapuri, A. (2006, October). Music structure analysis by finding repeated parts. In Proceedings of the 1st ACM workshop on Audio and music computing multimedia (pp. 59-68).

[9] utilizes DFT on pitch-class sets and constructs a Fourier phase space to analyze the harmonic language of Schubert. 
[10] analyzes the harmonic structure based on pitch scapes.
[11] proposes a generative syntax of diatonic harmonic progressions based on linguistic approaches and on the GTTM, modeling a hierarchical harmonic structure.
[12] works on the acoustic signal to find music structure. After analyzing the signal, a set of segments are generated as ground truth, the authors construct the music structure by matching the segments in a music piece to the ground truth segments.

The analysis of [9] mainly focuses on music of Schubert.  [9, 10, 12] analyze the music structure regarding one aspect of the music, however we aim to build structures based on different features we can extract from the music piece and figure out the relations between different result structures. [11] generates structure for diatonic harmony, but Debussy’s works contain non-tonal and non-functional elements, it would be interesting looking into the structure of such music.
