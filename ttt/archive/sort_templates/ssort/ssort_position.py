import question_template

game_type = 'input_output'
source_language = 'C'

parameter_list = [
	['$y0','string'],
	['$y1','string'],
	['$y2','string'],
]

tuple_list = [
	['ssort_position_',
		[None,None,None],
	]
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx
dx	void selection_sort(int a[], int n)
dx	{
dx		int i,j,temp;
dx
dx		for (i = 0; i < n-1; i++) {
dx			printf("%i\\n",a[2]);
dx			for (j = i + 1; j < n; j++) {
dx				if (a[i] > a[j]) {
dx					temp = a[i];
dx					a[i] = a[j];
dx					a[j] = temp;
dx				}
dx			}
dx		}
dx	}
'''

main_code_template = '''\
dx		int a[4] = {1,3,2,4};
dx
dx		selection_sort(a,4);        
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$y0
$y1
$y2
'''

question = question_template.Question_template(game_type,source_language,
 parameter_list,tuple_list,global_code_template,main_code_template,
 argv_template,stdin_template,stdout_template)


