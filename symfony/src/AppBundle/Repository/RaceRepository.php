<?php

namespace AppBundle\Repository;

use Doctrine\ORM\EntityRepository;

class RaceRepository extends EntityRepository
{

    public function filter($request)
    {
        // {{{

        $qb = $this->getEntityManager()->createQueryBuilder();

        $qb->select('r')
            ->from('AppBundle:Race', 'r')
            ->where('r.deletedAt is null')
            ->orderBy('r.id', 'ASC')
            ;

        if ($request->query->get('specie')) {
            $qb->andWhere('r.specie = :specie');
            $qb->setParameter('specie', $request->query->get('specie'));
        }

        return $qb->getQuery()->getResult();

        // }}}
    }

}
