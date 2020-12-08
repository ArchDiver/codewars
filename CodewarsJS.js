// // function martingale(bank, outcomes){
// //     let stake = 100;
// //     let i;
// //     for (i = 0; i < outcomes.length; i++){
// //         if(outcomes[i] == 1){
// //             bank += stake;
// //             stake = 100;
// //         }else {
// //             bank-=stake;
// //             stake *=2;
// //         }
// //     }
// //     return bank;
// // };

// // console.log(martingale(5100, [1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0]));

// // -----------------------------------------------------------------------------------------------------
// // Your Task
// // Complete the function to convert an integer into a string of the Turkish name.

// // input will always be an integer 0-99;
// // output should always be lower case.'
// '// Background
// // Forming the Turkish names for the numbers 0-99 is very straightforward:
// break;

// // units (0-9) and tens (10, 20, 30, etc.) each have their own unique name;
// // all other numbers are simply [tens] + [unit], like twenty one in English.
// // Unlike English, Turkish does not have "teen"-suffixed numbers; e.g. 13 would be directly translated as "ten three" rather than "thirteen" in English.

// // Turkish names of units and tens are as follows:

// // 0 = sıfır
// // 1 = bir
// // 2 = iki
// // 3 = üç
// // 4 = dört
// // 5 = beş
// // 6 = altı
// // 7 = yedi
// // 8 = sekiz
// // 9 = dokuz

// // 10 = on
// // 20 = yirmi
// // 30 = otuz
// // 40 = kırk
// // 50 = elli
// // 60 = altmış
// // 70 = yetmiş
// // 80 = seksen
// // 90 = doksan
// // Examples
// //  1  -->  "bir"
// // 13  -->  "on üç"
// // 27  -->  "yirmi yedi"
// // 38  -->  "otuz sekiz"
// // 77  -->  "yetmiş yedi"
// // 94  -->  "doksan dört"
// // Good luck, or iyi şanslar :)

// const getTurkishNumber = (num) => {
//   let numStr = String(num);
//   let turk = '';
//   while(numStr.length >1){
//     let numArr = numStr.split('');
//     numStr = numArr.pop();
//     var tens = numArr[0];
//     switch (tens){
//       case '1':
//         turk += 'on';
//         break;
//       case '2':
//         turk += 'yirmi';
//         break;
//       case '3':
//         turk += 'otuz';
//         break;
//       case '4': 
//         turk += 'kırk';
//         break;
//       case '5': 
//         turk += 'elli';
//         break;
//       case '6': 
//         turk += 'altmış';
//         break;
//       case '7': 
//         turk += 'yetmiş';
//         break;
//       case '8': 
//         turk += 'seksen';
//         break;
//       case '9': 
//         turk += 'doksan';
//         break;
//     }
//     if (numStr == 0){
//       numStr = '';
//     }else{
//       turk += ' ';
//     }
//   }
//   switch (numStr){
//     case '0':
//       turk += 'sıfır';
//       break;
//     case '1':
//       turk += 'bir';
//       break;
//     case '2':
//       turk += 'iki';
//       break;
//     case '3':
//       turk += 'üç';
//       break;
//     case '4':
//       turk += 'dört';
//       break;
//     case '5':
//       turk += 'beş';
//       break;
//     case '6':
//       turk += 'altı';
//       break;
//     case '7':
//       turk += 'yedi';
//       break;
//     case '8':
//       turk += 'sekiz';
//       break;
//     case '9':
//       turk += 'dokuz';
//       break;
//   }
//   return turk
// }

// getTurkishNumber(10);
// getTurkishNumber(2);
// getTurkishNumber(84);

// // ----------------------------------------------------------------------------
// Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

// It should remove all values from list a, which are present in list b.

// arrayDiff([1,2],[1]) == [2]
// If a value is present in b, all of its occurrences must be removed from the other:

// arrayDiff([1,2,2,2,3],[2]) == [1,3]
// Mine:
// function arrayDiff(a, b) {
//   let final;
//   for(var i = 0; i < b.length; i++){
//     console.log(b[i]);
//     for (var j = 0; j < a.length; j++){
//       console.log(a[j]);
//       if (b[i] == a[j]){
//         a.splice(j,1)
//         j -=1
//       };
//     };
//   };
//   return a;
// };

// console.log(arrayDiff([1,2],[1])); // == [2]
// console.log(arrayDiff([1,2,2,2,3],[2])); // == [1,3]

// // best:
// function array_diff(a, b) {
//   return a.filter(e => !b.includes(e));
// }

// // good:
// function array_diff(a, b) {
//   return a.filter(function(x) { return b.indexOf(x) == -1; });
// }
// ----------------------------------------------------------
// # Aug Aug 25  --> 
// # Whiteboard challenge - Find target (Binary Search)
// # Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums. If target exists, then return its index, otherwise return -1.
// # Example 1:
// # Input: nums = [-1,0,3,5,9,12], target = 9
// # Output: 4
// # Explanation: 9 exists in nums and its index is 4
// # Example 2:
// # Input: nums = [-1,0,3,5,9,12], target = 2
// # Output: -1
// # Explanation: 2 does not exist in nums so return -1

// function getTarget(arr, target){
//   let index;
//   for (var i = 0; i < arr.length; i++){
//     if (arr[i] == target){
//       index = i;
//       break;
//     }else{
//       index = -1
//     }
//   }
//   return index
// }

// console.log(getTarget([-1,0,3,5,9,12],2))
// console.log(getTarget([-1,0,3,5,9,12],9))
// ------------------------------

// // not working
// function getTarget(arr, target){
//   let min = 0;
//   let mid = Math.floor((arr.length/2));
//   let max = arr.length;
//   while (max>=min){
//     if ( target == arr[mid]){ //this needs to be corrected. 
//       return mid;
//     }else if( target < arr[mid]){
//       max = mid;
//       mid = max/2;
//     }else if (target > arr[mid]){
//       min = mid;
//       mid = (max-min)+min;
//     }else {
//       return -1
//     }
//   }
//}
// ------------------------------
// function getTarget(arr, target, min=0, max=arr.length - 1){
//   if (min > max){
//     return 'min > max'
//   }
//   let mid = Math.floor((min+max)/2);
//   if (arr[mid] === target){
//     return mid;
//   }
//   if(arr[mid] < target){
//     return getTarget(arr, target, mid+1, max);
//   } else if (arr[mid] > target){
//     return getTarget(arr, target, min, mid-1); 
//   }
//   return mid;
// }

// console.log(getTarget([-1,0,3,5,9,12],2))
// console.log(getTarget([-1,0,3,5,9,12],9))





// ------------------------------

//   let index;
//   let arrLen = arr.length
//   let midLen = Math.floor(arrLen/2);
//   let mid = arr[midLen];
//   let max = arrLen;
//   let min = 0
//   console.log(mid)
//   while (target > min && target < max {
//     if(target == mid){
//       return 
//     } else if (target > mid){
//       low = midLen;
//       mid = (Math.floor(max-mid))+ mid;
//     }else{

//     }



//   }
// }


// console.log(getTarget([-1,0,3,5,9,12],2))
// console.log(getTarget([-1,0,3,5,9,12],9))
// -------------------------------------------------------------------------------------------------------------------
// # Your plane has just landed in England and you rent a car. You have a meeting really soon and you have to get from Heathrow Airport to London as fast as you can.

// # There are two main roads going from Heathrow to London and there's a number of regional roads crossing them. It takes you a fixed amount of time to travel from one crossroads to another. It's up to you to find the optimal path to take so that you get to London as fast as you can! You start on the left side and can either cross to the other main road or go forward.

// # For example:

// #         |                                   |
// #        A|___50___|___05___|___40___|___10___|
// # AIRPORT |      30|      20|      25|        |  LONDON
// #        B|___10___|___90___|___02___|___08___|
// #         |                                   |
// # Each number denotes the minutes it takes to travel on that segment. The shortest path in this example is to start on road B, take the first left to road A, then take the first right back to road B, and then stay on road B until we get to London. This results in 10 + 30 + 5 + 20 + 2 + 8 = 75 minutes.

// # You need to write a function that accepts a road map and print out the shortest path. The road system will be an array of Sections for each A, B, and Crossover segment. Given the types:

// # data Section = Section { getA :: Int, getB :: Int, getC :: Int } deriving (Show)  
// # type RoadSystem = [Section]
// # the input for the above scenario would be

// # [Section 50 10 30, Section 5 90 20, Section 40 2 25, Section 10 8 0] 
// # To have the map neatly fit into Sections, we say that there's a last crossing section that takes 0 minutes to drive over. That's because we don't care where we arrive in London, as long as we're in London.

// # The function you define will return a Path where

// # data Label = A | B | C deriving (Show)  
// # type Path = [(Label, Int)]
// # In the example above, the correct Path would be

// # [(B,10),(C,30),(A,5),(C,20),(B,2),(B,8),(C,0)]
// # It's okay if your solution includes the last (C,0) tuple.

function optimalPath(road) {
  print(road);
  let path = [];
  let taken = 0;
  let notTaken = 1;
  let cross = 0;
  for (let i = 0; i < road.length; i++){
    print(road[i][0]);
    print(road[i][1]);
    print(road[i][2]);
    if ((road[i][notTaken] + cross) < road[i][taken]){
      path.append((road[i][notTaken] + cross))
      swap = taken;
      taken = notTaken;
      notTaken = swap;
      cross = road[i][2];
    }else{
      path.append(road[i][taken]);
      cross = road[i][2];
    }
  }
  return path;
}

print(optimalPath([ [50,10,30], [5,90,20], [40,2,25], [10,8,0] ]))

// --------------------------------------------------------------------------------------
