#include "lists.h"
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *p, *new, *temp;

	if (!head)
		return (NULL);

	p = *head;
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	
	if (!p)
	{
		*head = new;
		return (new);
	}
	if (p->n >= new->n)
	{
		new->next = p;
		*head = new;
		return (new);
	}

	while (p->next)
	{
		if (p->n <= new->n && p->next->n >= new->n)
		{
			temp = p->next;
			p->next = new;
			new->next = temp;

			return (new);
		}

		p = p->next;
	}
	p->next = new;
	new->next = NULL;

	return (new);
}
