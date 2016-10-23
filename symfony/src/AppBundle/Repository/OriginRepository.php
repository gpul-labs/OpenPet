<?php

namespace AppBundle\Repository;

use Doctrine\ORM\EntityRepository;

class OriginRepository extends EntityRepository
{

    public function filter($request)
    {
        // {{{

        $qb = $this->getEntityManager()->createQueryBuilder();

        $qb->select('o')
            ->from('AppBundle:Origin', 'o')
            ->where('o.deletedAt is null')
            ->orderBy('o.id', 'ASC')
            ;

        return $qb->getQuery()->getResult();

        // }}}
    }

}
