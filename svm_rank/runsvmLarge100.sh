#feature 5 minscore

#./svm_rank_learn -c 1 -t 0 -e 0.002 -d 2 -s 1 -l 2 /Users/apple/Desktop/hta/Courses/USC/MLandOpt/Project/CBSH2-master/featureMin5/featureMintrain.txt /Users/apple/Desktop/hta/Courses/USC/MLandOpt/Project/CBSH2-master/featureMin5/model


#./svm_rank_learn -c 0.1 -t 2 -d 2 -s 1 -l 2 /Users/apple/Desktop/hta/Courses/USC/MLandOpt/Project/CBSH2-master/featureMax5/featureMaxtrain.txt /Users/apple/Desktop/hta/Courses/USC/MLandOpt/Project/CBSH2-master/featureMax5/model

#./svm_rank_classify /Users/apple/Desktop/hta/Courses/USC/MLandOpt/Project/CBSH2-master/featureMin5/featureMintest.txt /Users/apple/Desktop/hta/Courses/USC/MLandOpt/Project/CBSH2-master/featureMin5/model /Users/apple/Desktop/hta/Courses/USC/MLandOpt/Project/CBSH2-master/featureMin5/predictions





#feature 5 maxscore

#./svm_rank_learn -c 10 -t 0 -e 0.0077 -d 2 -s 1 -l 2 /Users/apple/Desktop/hta/Courses/USC/MLandOpt/Project/CBSH2-master/featureMax5/featureMaxtrain.txt /Users/apple/Desktop/hta/Courses/USC/MLandOpt/Project/CBSH2-master/featureMax5/model  #swap 10.18%    loss: 27.43%


./svm_rank_learn -c 200 -t 3 -e 0.0001 -d 2 -s 1 -r 1 -l 2 /Users/apple/Desktop/hta/Courses/USC/MLandOpt/Project/CBSH2-master/featureLarge100/featureLarge100_train.txt /Users/apple/Desktop/hta/Courses/USC/MLandOpt/Project/CBSH2-master/featureLarge100/model2

#./svm_rank_learn -c 0.1 -t 2 -d 2 -s 1 -l 2 /Users/apple/Desktop/hta/Courses/USC/MLandOpt/Project/CBSH2-master/featureMax5/featureMaxtrain.txt /Users/apple/Desktop/hta/Courses/USC/MLandOpt/Project/CBSH2-master/featureMax5/model

./svm_rank_classify /Users/apple/Desktop/hta/Courses/USC/MLandOpt/Project/CBSH2-master/featureLarge100/featureLarge100_test.txt /Users/apple/Desktop/hta/Courses/USC/MLandOpt/Project/CBSH2-master/featureLarge100/model2 /Users/apple/Desktop/hta/Courses/USC/MLandOpt/Project/CBSH2-master/featureLarge100/predictions


