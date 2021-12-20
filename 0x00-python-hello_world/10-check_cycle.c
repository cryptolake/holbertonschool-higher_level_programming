#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *p = list;
	listint_t *arr[100];
	size_t i = 0, j;

	while (p)
	{
		
		arr[i] = p;
		for (j = 0; j <= i; j++) 
			if (p->next == arr[j])
				return (1);

		p = p->next;
		i++;
	}

	return (0);
}
