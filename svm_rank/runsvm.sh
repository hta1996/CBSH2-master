#feature 5 combined oracle

./svm_rank_learn -c 5000 -t 0 -e 0.0001 -d 2 -s 1 -l 2 /Users/apple/Desktop/hta/Courses/USC/MLandOpt/Project/CBSH2-master/featureMax5/featureCombtrain.txt /Users/apple/Desktop/hta/Courses/USC/MLandOpt/Project/CBSH2-master/featureMax5/modelcombined

#./svm_rank_learn -c 0.1 -t 2 -d 2 -s 1 -l 2 /Users/apple/Desktop/hta/Courses/USC/MLandOpt/Project/CBSH2-master/featureMax5/featureMaxtrain.txt /Users/apple/Desktop/hta/Courses/USC/MLandOpt/Project/CBSH2-master/featureMax5/model

./svm_rank_classify /Users/apple/Desktop/hta/Courses/USC/MLandOpt/Project/CBSH2-master/featureMax5/featureCombtest.txt /Users/apple/Desktop/hta/Courses/USC/MLandOpt/Project/CBSH2-master/featureMax5/modelcombined /Users/apple/Desktop/hta/Courses/USC/MLandOpt/Project/CBSH2-master/featureMax5/predictions


sleep 720000


./svm_rank_classify /Users/apple/Desktop/hta/Courses/USC/MLandOpt/Project/CBSH2-master/featureMax3/featureMaxtest.txt /Users/apple/Desktop/hta/Courses/USC/MLandOpt/Project/CBSH2-master/featureMax/mode2 /Users/apple/Desktop/hta/Courses/USC/MLandOpt/Project/CBSH2-master/featureMax3/predictions

#combined 3 and 5
./svm_rank_learn -c 5000 -t 0 -e 0.0001 -d 2 -s 1 -l 2 /Users/apple/Desktop/hta/Courses/USC/MLandOpt/Project/CBSH2-master/featureMax/featureMaxtrain.txt /Users/apple/Desktop/hta/Courses/USC/MLandOpt/Project/CBSH2-master/featureMax/mode2

#./svm_rank_learn -c 0.1 -t 2 -d 2 -s 1 -l 2 /Users/apple/Desktop/hta/Courses/USC/MLandOpt/Project/CBSH2-master/featureMax5/featureMaxtrain.txt /Users/apple/Desktop/hta/Courses/USC/MLandOpt/Project/CBSH2-master/featureMax5/model

./svm_rank_classify /Users/apple/Desktop/hta/Courses/USC/MLandOpt/Project/CBSH2-master/featureMax/featureMaxtest.txt /Users/apple/Desktop/hta/Courses/USC/MLandOpt/Project/CBSH2-master/featureMax/mode2 /Users/apple/Desktop/hta/Courses/USC/MLandOpt/Project/CBSH2-master/featureMax/predictions



#feature 3 combined oracle

#./svm_rank_learn -c 5000 -t 0 -e 0.0001 -d 2 -s 1 -l 2 /Users/apple/Desktop/hta/Courses/USC/MLandOpt/Project/CBSH2-master/featureMax3/featureMaxtrain.txt /Users/apple/Desktop/hta/Courses/USC/MLandOpt/Project/CBSH2-master/featureMax3/mode2

#./svm_rank_learn -c 0.1 -t 2 -d 2 -s 1 -l 2 /Users/apple/Desktop/hta/Courses/USC/MLandOpt/Project/CBSH2-master/featureMax5/featureMaxtrain.txt /Users/apple/Desktop/hta/Courses/USC/MLandOpt/Project/CBSH2-master/featureMax5/model

#./svm_rank_classify /Users/apple/Desktop/hta/Courses/USC/MLandOpt/Project/CBSH2-master/featureMax3/featureMaxtest.txt /Users/apple/Desktop/hta/Courses/USC/MLandOpt/Project/CBSH2-master/featureMax3/mode2 /Users/apple/Desktop/hta/Courses/USC/MLandOpt/Project/CBSH2-master/featureMax3/predictions




#feature 5 combined oracle

#./svm_rank_learn -c 5000 -t 0 -e 0.0001 -d 2 -s 1 -l 2 /Users/apple/Desktop/hta/Courses/USC/MLandOpt/Project/CBSH2-master/featureMax5/featureMaxtrain.txt /Users/apple/Desktop/hta/Courses/USC/MLandOpt/Project/CBSH2-master/featureMax5/mode2

#./svm_rank_learn -c 0.1 -t 2 -d 2 -s 1 -l 2 /Users/apple/Desktop/hta/Courses/USC/MLandOpt/Project/CBSH2-master/featureMax5/featureMaxtrain.txt /Users/apple/Desktop/hta/Courses/USC/MLandOpt/Project/CBSH2-master/featureMax5/model

#./svm_rank_classify /Users/apple/Desktop/hta/Courses/USC/MLandOpt/Project/CBSH2-master/featureMax5/featureMaxtest.txt /Users/apple/Desktop/hta/Courses/USC/MLandOpt/Project/CBSH2-master/featureMax5/mode2 /Users/apple/Desktop/hta/Courses/USC/MLandOpt/Project/CBSH2-master/featureMax5/predictions





#feature 5 maxscore

#./svm_rank_learn -c 10 -t 0 -e 0.0077 -d 2 -s 1 -l 2 /Users/apple/Desktop/hta/Courses/USC/MLandOpt/Project/CBSH2-master/featureMax5/featureMaxtrain.txt /Users/apple/Desktop/hta/Courses/USC/MLandOpt/Project/CBSH2-master/featureMax5/model  #swap 10.18%    loss: 27.43%


#./svm_rank_learn -c 20 -t 0 -e 0.001 -d 2 -s 1 -r 1 -l 2 /Users/apple/Desktop/hta/Courses/USC/MLandOpt/Project/CBSH2-master/featureMax5/featureMaxtrain.txt /Users/apple/Desktop/hta/Courses/USC/MLandOpt/Project/CBSH2-master/featureMax5/model  #swap 10.18%    loss: 27.43%

#./svm_rank_learn -c 0.1 -t 2 -d 2 -s 1 -l 2 /Users/apple/Desktop/hta/Courses/USC/MLandOpt/Project/CBSH2-master/featureMax5/featureMaxtrain.txt /Users/apple/Desktop/hta/Courses/USC/MLandOpt/Project/CBSH2-master/featureMax5/model

#./svm_rank_classify /Users/apple/Desktop/hta/Courses/USC/MLandOpt/Project/CBSH2-master/featureMax5/featureMaxtest.txt /Users/apple/Desktop/hta/Courses/USC/MLandOpt/Project/CBSH2-master/featureMax5/model /Users/apple/Desktop/hta/Courses/USC/MLandOpt/Project/CBSH2-master/featureMax5/predictions


