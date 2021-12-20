#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *p = list;
	listint_t *pp;

	while (p)
	{
		pp = p->next;
		while (pp)
		{
			if (pp == p)
				return (1);
			pp = pp->next;
		}

		p = p->next;
	}

	return (0);
}
