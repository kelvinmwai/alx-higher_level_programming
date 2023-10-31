#include "lists.h"

/**
 * insert_node - Inserts new number to sorted linked list
 * @head: pointer to linked list head
 * @number: number to be inserted
 *
 * Return: Pointer to the new node | NULL if function fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (node == NULL || new->n < node->n)
	{
		new->next = node;
		return (*head = new);
	}

	while (node)
	{
		if (!node->next || new->n < node->next->n)
		{
			new->next = node->next;
			node->next = new;
			return (node);
		}
		node = node->next;
	}
	return (NULL);
}
